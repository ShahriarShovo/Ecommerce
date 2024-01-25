from django.contrib import admin
from products.models.products_model import Products ,Customer_Review,Coupon_Code
from products.models.old_product_variation import Variation
#from products.models.customer_review import Customer_Review
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.delivery_country import Product_Delivery_Country
from products.models.product_gallary import Product_Gallery

# Register your models here.

class Product_Gallery_Inline(admin.TabularInline):
    model = Product_Gallery
    extra=1

class Product_Admin(admin.ModelAdmin):
    inlines =[Product_Gallery_Inline]

admin.site.register(Products,Product_Admin)
admin.site.register(Customer_Review)
admin.site.register(Variation)
admin.site.register(Product_Size_variant)
admin.site.register(Product_Color_Variant)
admin.site.register(Product_Delivery_Country)
admin.site.register(Coupon_Code)
admin.site.register(Product_Gallery)
