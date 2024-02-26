from django import template
from cart.models.cart_item import Cart_Item
from cart.models.wish_list import Wish_List
from orders.models.product_ordered import Products_Ordered

register = template.Library()



@register.filter
def total_orders(product):
    return Products_Ordered.objects.filter(product_name=product).count()




