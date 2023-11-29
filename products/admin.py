from django.contrib import admin
from products.models.models import Products
from products.models.customer_review import Customer_Review

# Register your models here.

admin.site.register(Products)
admin.site.register(Customer_Review)