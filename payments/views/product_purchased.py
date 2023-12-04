from orders.models.orders import Order
from cart.models.cart import Cart
from django.shortcuts import render, HttpResponseRedirect,redirect
from django.urls import reverse
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from products.models.products_model import Products
import datetime


# global_dict={}
# print("Gblobal +++++++++++++", global_dict)
# array=[]
# print("Gblobal Arrya +++++++++++++", array)

def product_purchased(request,val_id, tran_id,total_amount):


    if request.user.is_authenticated:
        
        user = request.user
        user_address = BillingAddress.objects.get(user=user)
        cart_items = Cart.objects.filter(user=user, purchased=False)
        print("Cart item +++++++++++++++", cart_items)
        total_tax=request.session['total_tax'] 
        total_item_price=request.session['total_item_price']
        order_object_invoice=cart_items
        # global_dict.update(order_object_invoice)
        #array.append(cart_items)
        

        
        order = Order(user=user,
                      ordered=True,
                      paymentId=val_id,
                      orderId=tran_id,
                      final_total =total_amount,
                      total_tax=total_tax,
                      sum_of_each_product=total_item_price)
        
        get_payment_id = Order.objects.filter(paymentId=val_id)

        if len(get_payment_id) == 0 :

            order.save()

        else:
             print(" Nothing+++++++++++++")

        print("get_payment_id+++++++++",get_payment_id)
        
        
        for item in cart_items:
            item.purchased = True
            item.select_order_stats=1
            item.save()
        
        return render(request, 'messages/thank_you_for_purchased.html', locals())
    
    else:

        #user_address = BillingAddress.objects.get(user=user)
        cart_items = Cart.objects.filter(guest_user=False, purchased=False)
        print("Cart item anonomous +++++++++++++++++",cart_items)
        total_tax=request.session['total_tax'] 
        total_item_price=request.session['total_item_price']
        order_object_invoice=cart_items

        print("Cart item anonomous user +++++++++++++++++",order_object_invoice)

        cus_name = request.session['first_name']
        email = request.session['email']
        phone = request.session['phone']

        
        order = Order.objects.create(
                                    ordered=True,
                                    paymentId=val_id,
                                    orderId=tran_id,
                                    final_total =total_amount,
                                    total_tax=total_tax,
                                    sum_of_each_product=total_item_price)
        for item in cart_items:
            item.purchased = True
            item.select_order_stats=1
            item.guest_user=True
            item.save()
        
        return render(request, 'messages/thank_you_for_purchased.html', locals())





    
