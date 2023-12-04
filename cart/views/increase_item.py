from django.shortcuts import get_object_or_404 , redirect
from cart.models.cart import Cart
from products.models.products_model import Products


def increase_cart(request,pk):
    product = get_object_or_404(Products, pk=pk)

    if request.user.is_authenticated:

        current_item = Cart.objects.filter(item=product, user=request.user, purchased=False)[0]
        if current_item.quantity >=1:
            current_item.quantity+=1
            current_item.save()
            return redirect("cart_view")
        else:    
            return redirect("index")
        

    else:
        
        current_item = Cart.objects.filter(item=product, guest_user=True, purchased=False)[0]
        if current_item.quantity >=1:
            current_item.quantity+=1
            current_item.save()
            return redirect("cart_view")
        else:    
            return redirect("index")


        
    




