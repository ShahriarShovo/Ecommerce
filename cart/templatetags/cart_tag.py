from django import template
from cart.models.cart_item import Cart_Item
from cart.models.wish_list import Wish_List
from orders.models.product_ordered import Products_Ordered

register = template.Library()


@register.filter
def cart_total(user):

    #print( "user +++++++++++++++",user)
    cart_total_item = Cart_Item.objects.filter(cart__user=user, cart__is_paid=False)
    return cart_total_item.count()



@register.filter
def wish_list_total(user):

    #print("user+++++++++++", user)

    #print( "user +++++++++++++++",user)
    wishlist_total_item = Wish_List.objects.filter(user=user, is_added=True)
    return wishlist_total_item.count()

# @register.filter
# def total_orders(product):
#     return Products_Ordered.objects.filter(product_name=product).count()




