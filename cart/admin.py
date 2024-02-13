from django.contrib import admin
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from cart.models.wish_list import Wish_List


# Register your models here.

admin.site.register(Cart)
admin.site.register(Cart_Item)
admin.site.register(Wish_List)

 