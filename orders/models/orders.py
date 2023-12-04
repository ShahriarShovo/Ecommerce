from django.db import models
from products.models.products_model import Products
from cart.models.cart import Cart
from django.conf import settings
from user_auth.models.guest_user import Guest_User

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    guest_user = models.ForeignKey(Guest_User, on_delete=models.CASCADE, null=True, blank=True)
    orderItems = models.ManyToManyField(Cart, related_name='carts')
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    sum_of_each_product = models.FloatField(max_length=200, blank=True, null=True)
    total_tax = models.FloatField(max_length=200, blank=True, null=True)
    final_total= models.FloatField(max_length=200, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.paymentId
    

        
    
    
