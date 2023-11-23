from django.db import models
from products.models.models import Products
from cart.models.cart import Cart
from django.conf import settings

class Order(models.Model):

   
    PENDING=1
    DELIVER=2
    CANCLE=3
    oder_status = ((CANCLE, 'Cancle'), (DELIVER,'Deliver'), (PENDING,'Pending'))
    orderItems = models.ManyToManyField(Cart, related_name='carts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    select_order_stats = models.PositiveSmallIntegerField(choices=oder_status, blank=True, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.email
    

    def get_total_tax(self):
        total_tax=0
        for item_total_tax in self.orderItems.all():
            total_tax+= float(item_total_tax.calculate_tax())
        print('Tax -----------------------', total_tax)
        return total_tax

    def get_totals(self):
        total = 0
        tax = 0
        for order_item in self.orderItems.all():

            total+= float(order_item.get_total())
            tax += float(order_item.calculate_tax())

            #final_cost = total + tax

        return total
    
    def get_total_cost(self):

        final_toal = self.get_total_tax() +  self.get_totals()
        print("Final total -------", final_toal)

        return final_toal
        
    
    
