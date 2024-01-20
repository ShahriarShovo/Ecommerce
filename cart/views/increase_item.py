from django.shortcuts import get_object_or_404 , redirect
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from products.models.products_model import Products


def increase_cart(request,pk):
    product = get_object_or_404(Products, pk=pk)
    current_item = Cart_Item.objects.filter(product=product, cart__user=request.user, cart__is_paid=False)[0]
    if current_item.quantity >=1:
        current_item.quantity+=1
        current_item.save()
        return redirect("cart_view")
    else:    
        return redirect("index")

    # if request.user.is_authenticated:

    #     current_item = Cart_Item.objects.filter(product=product, user=request.user, cart__is_paid=False)[0]
    #     if current_item.quantity >=1:
    #         current_item.quantity+=1
    #         current_item.save()
    #         return redirect("cart_view")
    #     else:    
    #         return redirect("index")
        

    # else:
        
    #     current_item = Cart.objects.filter(item=product, guest_user=True, purchased=False)[0]
    #     if current_item.quantity >=1:
    #         current_item.quantity+=1
    #         current_item.save()
    #         return redirect("cart_view")
    #     else:    
    #         return redirect("index")


        
    




