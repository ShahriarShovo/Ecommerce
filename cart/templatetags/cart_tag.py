from django import template
from cart.models.cart import Cart

register = template.Library()


@register.filter
def cart_total(user):

    if user == None:
        cart_total_item = Cart.objects.filter(user=None, purchased=False)
        print(" without user +++++++++++++++++++++", cart_total_item)
        return cart_total_item.count()
    
    else:
        cart_total_item = Cart.objects.filter(user=user, purchased=False)
        return cart_total_item.count()



