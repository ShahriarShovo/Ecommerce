from django.contrib import admin
from product_categories.models.product_category import Product_Categories
from product_categories.models.product_brand import Product_Brand

# Register your models here.

admin.site.register(Product_Categories)
admin.site.register(Product_Brand)
