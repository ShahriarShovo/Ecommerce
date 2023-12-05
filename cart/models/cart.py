from django.db import models
from products.models.products_model import Products
from django.conf import settings
from user_auth.models.guest_user import Guest_User

# Create your models here.

class Cart(models.Model):

    PENDING=1
    DELIVER=2
    CANCLE=3
    oder_status = ((CANCLE, 'Cancle'), (DELIVER,'Deliver'), (PENDING,'Pending'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    purchased = models.BooleanField(default=False)
    guest_user = models.BooleanField(default=False)
    #guest_user = models.ForeignKey(Guest_User, on_delete=models.CASCADE, related_name="cart", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updatedd = models.DateTimeField(auto_now=True)
    select_order_stats = models.PositiveSmallIntegerField(choices=oder_status, blank=True, null=True)

    def __str__(self):
        #return str(self.id)
        return f'{self.quantity} X {self.item}'
    
    

    def get_total(self):
        total = self.item.product_price * self.quantity
        float_total = format( total, '0.2f')
        # print(' cart each_total -----------------------', float_total)
        return float_total
    

    

    
    
    


    
    

    


