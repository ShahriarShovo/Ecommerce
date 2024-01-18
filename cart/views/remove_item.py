from django.shortcuts import render, get_object_or_404 , redirect,HttpResponseRedirect
from cart.models.cart import Cart,Cart_Item
from orders.models.orders import Order
from products.models.products_model import Products




def remove_from_cart(request,pk):

    product = get_object_or_404(Products, pk=pk)
    item_cart = Cart_Item.objects.filter(product=product, cart__user=request.user, cart__is_paid=False)[0]
    
    if item_cart :
        remove_item = item_cart.delete()
        # print(" remove_item in cart ----", remove_item)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect("index")

# def remove_from_cart(request,pk):

#     product = get_object_or_404(Products, pk=pk)
#     item_cart = Cart_Item.objects.filter(product=product, cart__user=request.user, cart__is_paid=False)[0]
#     cart = Cart.objects.filter(user=request.user, is_paid=False)[0]
#     if item_cart and cart:
#         remove_item = item_cart.delete()
#         remove_item_cart = cart.delete()
#         # print(" remove_item in cart ----", remove_item)
#         return redirect("cart_view")
#     else:
#         return redirect("index")





    # if request.user.is_authenticated:
    #     item_in_cart = Cart.objects.filter(user= request.user, item=product, purchased=False)[0]
    #     # print(" item in cart ----", item_in_cart)
    #     if item_in_cart:
    #         remove_item = item_in_cart.delete()
    #         # print(" remove_item in cart ----", remove_item)
    #         return redirect("cart_view")
    #     else:
    #         return redirect("index")
    
    # else:

    #     item_in_cart = Cart.objects.filter(guest_user=True, item=product, purchased=False)[0]
    #     # print(" item in cart ----", item_in_cart)
    #     if item_in_cart:
    #         remove_item = item_in_cart.delete()
    #         # print(" remove_item in cart ----", remove_item)
    #         return redirect("cart_view")
    #     else:
    #         return redirect("index")



