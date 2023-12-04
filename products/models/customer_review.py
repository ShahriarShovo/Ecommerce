from django.db import models
from products.models.products_model import Products
from user_auth.models.user import User




class Customer_Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_review')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products_review')
    comment_area = models.TextField(blank=True, null=True)
    commented_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email