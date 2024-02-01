from django.db import models
from products.models.products_model import Products
from orders.models.orders import Order


class Products_Ordered(models.Model):
    ordered = models.ForeignKey(Order,on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    each_product_price = models.FloatField(null=True,blank=True)

    def __str__(self) -> str:
        return self.product_name.product_name