from django.shortcuts import render, get_object_or_404 , redirect, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products




# Create your views here.

def add_to_cart(request, pk):

    product_item = get_object_or_404(Products, pk=pk)

    if request.user.is_authenticated:

        cart_item = Cart.objects.filter(user=request.user, item=product_item,  purchased = False).first()
        if cart_item:
            cart_item.quantity +=1
            cart_item.save()
            return redirect("index")
        else:
            Cart.objects.create(item=product_item, user= request.user, purchased = False)
            return redirect("index")
        
        
    else:
        
        user=request.user.id
        print("Guest user id -----------------********************", user)
        cart_item = Cart.objects.filter(item=product_item, guest_user=True,  purchased = False).first()
        if cart_item:
            cart_item.quantity +=1
            cart_item.save()
            return redirect("index")
        else:
            Cart.objects.create(item=product_item,guest_user=True, purchased = False)

            return redirect("index")




#Old code 
# def add_to_cart(request, pk):
#     item = get_object_or_404(Products, pk=pk)
#     order_item = Cart.objects.get_or_create(item=item, user= request.user, purchased = False)
#     order_qs = Order.objects.filter(user = request.user , ordered = False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.orderItems.filter(item=item).exists():
#             order_item[0].quantity +=1
#             order_item[0].save()
#             return redirect("index")
#         else:
#             order.orderItems.add(order_item[0])
#             return redirect("index")
#     else:
#         order = Order(user= request.user)
#         order.save()
#         order.orderItems.add(order_item[0])
#         return redirect("index")
    

    




    









    









