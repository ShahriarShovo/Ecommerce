from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon_Code(models.Model):
    code = models.CharField(max_length=15, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    active_coupon_code = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Coupon Code"

    def __str__(self) -> str:
        return self.code