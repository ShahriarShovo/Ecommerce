from django.db import models


class Product_Color_Variant(models.Model):
    color_name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.color_name