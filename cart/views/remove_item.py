from django.shortcuts import render, get_object_or_404 , redirect
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products



def remove_from_cart(request,pk):

    product = get_object_or_404(Products, pk=pk)

    if request.user.is_authenticated:
        item_in_cart = Cart.objects.filter(user= request.user, item=product, purchased=False)[0]
        # print(" item in cart ----", item_in_cart)
        if item_in_cart:
            remove_item = item_in_cart.delete()
            # print(" remove_item in cart ----", remove_item)
            return redirect("cart_view")
        else:
            return redirect("index")
    
    else:

        item_in_cart = Cart.objects.filter(guest_user=True, item=product, purchased=False)[0]
        # print(" item in cart ----", item_in_cart)
        if item_in_cart:
            remove_item = item_in_cart.delete()
            # print(" remove_item in cart ----", remove_item)
            return redirect("cart_view")
        else:
            return redirect("index")



