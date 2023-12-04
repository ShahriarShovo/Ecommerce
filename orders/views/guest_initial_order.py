from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress
from user_auth.models.guest_user import Guest_User

def guest_initial_order(request):
     
    pass