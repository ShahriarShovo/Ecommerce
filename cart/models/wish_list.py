from django.db import models
from products.models.products_model import Products
from django.conf import settings


class Wish_List(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wish_list", null=True, blank=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, related_name='wish_list')
    is_added = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.products.product_name


