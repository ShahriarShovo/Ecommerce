from django.shortcuts import render, get_object_or_404 , redirect, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products




# Create your views here.

def add_to_cart(request, pk):

    product_item = get_object_or_404(Products, pk=pk)

    if request.user.is_authenticated:

        cart_item = Cart.objects.filter(user=request.user, item=product_item,  purchased = False).first()

        size=request.POST.get('size')
        color=request.POST.get('color')
        quantity= request.POST.get('quantity')

        # print("Size ===================", size)
        # print("Color ===================", color)
        # print("quantity ===================", quantity)


        if cart_item:

            if quantity:

                cart_item.quantity += int(quantity)
            else:

                cart_item.quantity +=1
            
            cart_item.color=color
            cart_item.size=size
            cart_item.save()
            return redirect("index")
        
        else:
            Cart.objects.create(item=product_item,color=color,size=size, quantity=quantity, user= request.user, purchased = False)
            return redirect("index")
        
        
    else:
        
        user=request.user.id
        print("Guest user id -----------------********************", user)
        cart_item = Cart.objects.filter(item=product_item, guest_user=True,  purchased = False).first()

        size=request.POST.get('size')
        color=request.POST.get('color')
        quantity= request.POST.get('quantity')

        print("Size ===================", size)
        print("Color ===================", color)
        print("quantity ===================", quantity)

        if cart_item:
            if quantity:
                cart_item.quantity += int(quantity)
            else:
                cart_item.quantity +=1
            cart_item.color=color
            cart_item.size=size
            cart_item.save()
            return redirect("index")
        else:
            Cart.objects.create(item=product_item,guest_user=True,color=color,size=size,quantity=quantity, purchased = False)

            return redirect("index")


    

    




    









    









