
from django.shortcuts import get_object_or_404 , redirect
from cart.models.cart import Cart, Cart_Item
from django.http import HttpResponseRedirect

from products.models.products_model import Products

def decrease_cart(request,pk):
    product = get_object_or_404(Products, pk=pk)
    current_item = Cart_Item.objects.filter(product=product, cart__user=request.user, cart__is_paid=False)[0]
    #current_item = Cart.objects.filter(item=product, user=request.user, purchased=False)[0]
    if current_item.quantity > 1:
        current_item.quantity-=1
        current_item.save()
        #return redirect("cart_view")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        current_item.delete()   
        return redirect("index")

    # if request.user.is_authenticated:
        
    #     current_item = Cart.objects.filter(item=product, user=request.user, purchased=False)[0]
    #     if current_item.quantity > 1:
    #         current_item.quantity-=1
    #         current_item.save()
    #         #return redirect("cart_view")
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #     else:
    #         current_item.delete()   
    #         return redirect("index")
    
    # # else:

    # #     current_item = Cart.objects.filter(item=product, guest_user=True, purchased=False)[0]
    # #     if current_item.quantity > 1:
    # #         current_item.quantity-=1
    # #         current_item.save()
    # #         return redirect("cart_view")
    # #     else:
    # #         current_item.delete()   
    # #         return redirect("index")


