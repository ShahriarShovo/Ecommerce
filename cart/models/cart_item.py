from django.db import models
from products.models.products_model import Products, Coupon_Code
from django.conf import settings
from user_auth.models.guest_user import Guest_User
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.products_model import Coupon_Code
from cart.models.cart import Cart



class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    product_Size_variant = models.ForeignKey(Product_Size_variant, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def get_product_price(self):
        price = [self.product.product_price]
        if self.product_Size_variant:
            size_variant_price = self.product_Size_variant.price
            price.append(size_variant_price )
        return sum(price) * self.quantity
    
    def __str__(self) -> str:
        return self.product.product_name