from django.urls import path, include
#from cart.views.old_add_to_cart import add_to_cart
from cart.views.add_to_cart import add_to_cart
from cart.views.cart_view import cart_view
from cart.views.increase_item import increase_cart
from cart.views.decrease_item import decrease_cart
from cart.views.remove_item import remove_from_cart
from cart.views.clear_cart import clear_cart
from cart.views.add_to_wish_list import add_to_wish_list
from cart.views.view_wishlist import view_wish_list




urlpatterns = [
    
     path('add/<int:pk>/', add_to_cart, name='add_to_cart'), 
     path('view/', cart_view, name='cart_view'),
     path('increase_item/<int:pk>/', increase_cart, name="increase_item"),
     path('decrease_item/<int:pk>/', decrease_cart, name="decrease_item"),
     path('remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
     path('clear/', clear_cart, name='clear_cart'),
     path('check_out/', include('orders.urls')),

     path('wish-list/<int:pk>/', add_to_wish_list, name="add_to_wish_list"),

     path('view-wish-list/', view_wish_list, name="view_wish_list"),



]
