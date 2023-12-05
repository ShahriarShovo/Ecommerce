from django.contrib import admin
from products.models.products_model import Products, Variation
from products.models.customer_review import Customer_Review

# Register your models here.

admin.site.register(Products)
admin.site.register(Customer_Review)
admin.site.register(Variation)