from django.db import models
from products.models.products_model import Products, Coupon_Code
from django.conf import settings
from user_auth.models.guest_user import Guest_User
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.products_model import Coupon_Code



# Create your models here.

class Cart (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon_Code, on_delete=models.SET_NULL, null=True, blank=True)

    def get_cart_total(self):
        cart_items= self.cart_item.all()
        price = []

        #print("Price ---------------------------------------------",price)

        for cart_item in cart_items:
            price.append(cart_item.product.product_price)
            if cart_item.product_Size_variant:
                size_variant_price = cart_item.product_Size_variant.price
                price.append(size_variant_price)
        
        if self.coupon:
            return sum(price) - self.coupon.discount
        
        return sum(price)
    
    def get_tax(self):
        total_tax= self.get_cart_total() * float(5/100)
        return total_tax
    
    def __str__(self) -> str:
        return self.user.email
    



class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    product_Size_variant = models.ForeignKey(Product_Size_variant, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1)

    def get_product_price(self):
        price = [self.product.product_price]
        if self.product_Size_variant:
            size_variant_price = self.product_Size_variant.price
            price.append(size_variant_price *self.quantity)
        return sum(price)
    
    def __str__(self) -> str:
        return self.product.product_name
    



# class Cart(models.Model):

#     PENDING=1
#     DELIVER=2
#     CANCLE=3
#     oder_status = ((CANCLE, 'Cancle'), (DELIVER,'Deliver'), (PENDING,'Pending'))
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
#     item = models.ForeignKey(Products, on_delete=models.CASCADE)
#     coupon_Code = models.ForeignKey(Coupon_Code, on_delete=models.SET_NULL, null=True, blank=True)
#     quantity = models.IntegerField(default=1)
#     price = models.FloatField(default=0)
   
#     purchased = models.BooleanField(default=False)
#     guest_user = models.BooleanField(default=False)
#     #guest_user = models.ForeignKey(Guest_User, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updatedd = models.DateTimeField(auto_now=True)
#     select_order_stats = models.PositiveSmallIntegerField(choices=oder_status, blank=True, null=True)
#     product_color = models.ForeignKey(Product_Color_Variant, on_delete=models.SET_NULL, blank=True, null=True)
#     product_size = models.ForeignKey(Product_Size_variant, on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         #return str(self.id)
#         return f'{self.quantity} X {self.item}'
    
    

#     def get_total(self):
#         total = self.price * self.quantity
#         float_total = format( total, '0.2f')
#         # print(' cart each_total -----------------------', float_total)
#         return float_total
    

    

    
    
    


    
    

    


