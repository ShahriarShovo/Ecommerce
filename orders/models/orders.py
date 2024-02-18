from django.db import models
from cart.models.cart import Cart
from django.conf import settings
from user_auth.models.guest_user import Guest_User

from products.models.product_variation.size_variant import Product_Size_variant
from orders.models.billing_address import BillingAddress
#from orders.models.product_ordered import Products_Ordered

class Order(models.Model):

    pay_status =(
        ('Paid', 'Paid'),
        ('Cash_on_delivery', 'Cash on delivery'),
    )

    order_status =(
        
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    order_number = models.CharField(max_length=200, null=True, blank=True)
    payment_number = models.CharField(max_length=200, null=True, blank=True)
    order_total = models.FloatField(null=True,blank=True)
    tax = models.FloatField(null=True,blank=True)
    grand_total = models.FloatField(null=True,blank=True)
    payment_status = models.CharField(choices=pay_status, default='Paid', max_length=50)
    status = models.CharField(choices=order_status, default='Pending', max_length=50)
    ip_address = models.CharField(max_length=200, blank=True, null=True)
    bank=models.CharField(max_length=20, null=True, blank=True)
    is_ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    

    def __str__(self) -> str:
        return self.order_number
    

        
    
    
