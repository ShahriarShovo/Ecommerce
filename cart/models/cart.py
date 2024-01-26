from django.db import models
from products.models.products_model import Products, Coupon_Code
from django.conf import settings
from user_auth.models.guest_user import Guest_User
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.products_model import Coupon_Code
from django.utils import timezone



# Create your models here.

class Cart (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon_Code, on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.CharField(max_length=255, unique=True,null=True)
    payment_id = models.CharField(max_length=255,unique=True,null=True)
    created = models.DateTimeField(default=timezone.now)

    #Another fuction using list comprehensive 

    def get_cart_total(self):
        
        cart_items= self.cart_item.all()

        # return sum( (item.product.product_price + item.product_Size_variant.price) * item.quantity
        #            if item.product_Size_variant else item.product.product_price  * item.quantity
        #             for item in cart_items 
        #                )

        final_total = sum((item.product.product_price + item.product_Size_variant.price) * item.quantity
                   if item.product_Size_variant else item.product.product_price  * item.quantity
                    for item in cart_items)
        
        #print("Final ---------------------------------------------",final_total)

        if self.coupon:
             return final_total - self.coupon.discount
        
        return final_total


    def get_tax(self):
        total_tax= self.get_cart_total() * float(5/100)
        return total_tax
    
    def get_fully_total(self):

        final_total = self.get_cart_total()
        tax = self.get_tax()
        total_final = final_total + tax

        #print("Final total ---------------------------------------------",total_final)
        return total_final
    
    def __str__(self) -> str:
        return self.user.email
    





    

    

    
    
    


    
    

    


