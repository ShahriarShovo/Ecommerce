from django import template
from cart.models.cart import Cart, Cart_Item

register = template.Library()


@register.filter
def cart_total(user):

    print( "user +++++++++++++++",user)
    cart_total_item = Cart_Item.objects.filter(cart__user=user, cart__is_paid=False)
    return cart_total_item.count()

    
    # if user == None:
    #     cart_total_item = Cart.objects.filter(user=None, purchased=False)
    #     print(" without user +++++++++++++++++++++", cart_total_item)
    #     return cart_total_item.count()
    
    # else:
    #     cart_total_item = Cart.objects.filter(user=user, purchased=False)
    #     return cart_total_item.count()



