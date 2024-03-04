from django import template
from orders.models.product_ordered import Products_Ordered

register = template.Library()



@register.filter
def total_orders(product):
    return Products_Ordered.objects.filter(product_name=product).count()




