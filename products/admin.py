from django.contrib import admin
from products.models.products_model import Products 
from products.models.old_product_variation import Variation
from products.models.customer_review import Customer_Review
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant

# Register your models here.

admin.site.register(Products)
admin.site.register(Customer_Review)
admin.site.register(Variation)
admin.site.register(Product_Size_variant)
admin.site.register(Product_Color_Variant)
