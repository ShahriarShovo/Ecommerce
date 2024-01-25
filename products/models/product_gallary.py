from django.db import models
from products.models.products_model import Products

class Product_Gallery(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='product_gallary', max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.product.product_name