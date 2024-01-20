from django.contrib import admin
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item


# Register your models here.

admin.site.register(Cart)
admin.site.register(Cart_Item)

 