from django.db import models


class Product_Size_variant(models.Model):
    size_name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.size_name