from django.db import models
from products.models.models import Products
from django.conf import settings

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updatedd = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return str(self.id)
        return f'{self.quantity} X {self.item}'
    
    def calculate_tax(self):
        tax = self.item.product_price * self.quantity * (5 / 100)
        float_tax = format( tax, '0.2f')
       
        return float_tax

    def get_total(self):
        total = self.item.product_price * self.quantity
        float_total = format( total, '0.2f')
        print(' cart float_total -----------------------', float_total)
        return float_total
    
    

    


