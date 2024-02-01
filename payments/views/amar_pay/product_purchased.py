
from django.shortcuts import render, HttpResponseRedirect,redirect
from django.urls import reverse
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from products.models.products_model import Products
import datetime
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


# global_dict={}
# print("Gblobal +++++++++++++", global_dict)
# array=[]
# print("Gblobal Arrya +++++++++++++", array)

def product_purchased(request,*args, **kwargs):


    if request.user.is_authenticated:

        user=request.user
        
        cart_items= Cart_Item.objects.filter(cart__user=request.user, cart__is_paid=False)
        cart_object = Cart.objects.filter(user=user, is_paid=False)
        get_total= [total.get_cart_total() for total in cart_object]
        get_tax= [tax.get_tax() for tax in cart_object]
        grand_total= [grand_total.get_fully_total() for grand_total in cart_object]


        save_order = Order()
        save_order.user=user
        save_order.order_number=kwargs['order_id']
        save_order.payment_number=kwargs['payment_id']
        save_order.order_total=float(get_total[0])
        save_order.tax=float(get_tax[0])
        save_order.grand_total=float(grand_total[0])
        save_order.payment_status='Paid'
        save_order.ip_address=kwargs['ip_address']
        save_order.bank=kwargs['card_type']
        save_order.is_ordered=True
        save_order.save()

        for items in cart_items:
            Products_Ordered.objects.create(
                ordered=save_order,
                product_name=items.product,
                quantity=items.quantity,
                product_Size_variant=items.product_Size_variant,
                each_product_price=items.get_product_price()
            )
       


        Cart_Item.objects.filter(cart__user=user).delete()
        return HttpResponseRedirect(reverse("invoice", kwargs={'pay_id':kwargs['payment_id'], 'order_id':kwargs['order_id']}))
    else:
        return HttpResponse("Cash on delivery is not working")
        
        
        # user = request.user
        # user_address = BillingAddress.objects.get(user=user)
        # cart_items = Cart.objects.filter(user=user, purchased=False)
        # print("Cart item +++++++++++++++", cart_items)
        # total_tax=request.session['total_tax'] 
        # total_item_price=request.session['total_item_price']
        # order_object_invoice=cart_items
       
        # order = Order(user=user,
        #               ordered=True,
        #               paymentId=val_id,
        #               orderId=tran_id,
        #               final_total =total_amount,
        #               total_tax=total_tax,
        #               sum_of_each_product=total_item_price)
        
        # get_payment_id = Order.objects.filter(paymentId=val_id)

        # if len(get_payment_id) == 0 :

        #     order.save()

        # else:
        #      print(" Nothing+++++++++++++")

        # print("get_payment_id+++++++++",get_payment_id)
        
        
        # for item in cart_items:
        #     item.purchased = True
        #     item.select_order_stats=1
        #     item.save()
        
        #return render(request, 'messages/thank_you_for_purchased.html', locals())
    
    # else:

    #     #user_address = BillingAddress.objects.get(user=user)
    #     cart_items = Cart.objects.filter(guest_user=True, purchased=False)
    #     print("Cart item anonomous +++++++++++++++++",cart_items)
    #     total_tax=request.session['total_tax'] 
    #     total_item_price=request.session['total_item_price']
    #     order_object_invoice=cart_items

    #     #print("Cart item anonomous user +++++++++++++++++",order_object_invoice)

    #     cus_name = request.session['first_name']
    #     email = request.session['email']
    #     phone = request.session['phone']

        
    #     order = Order(
    #                                 ordered=True,
    #                                 paymentId=val_id,
    #                                 orderId=tran_id,
    #                                 final_total =total_amount,
    #                                 total_tax=total_tax,
    #                                 sum_of_each_product=total_item_price)
        
    #     get_payment_id = Order.objects.filter(paymentId=val_id)

    #     if len(get_payment_id) == 0 :

    #         order.save()

    #     else:
    #          print(" Nothing+++++++++++++")
             
    #     for item in cart_items:
    #         item.purchased = True
    #         item.select_order_stats=1
    #         #item.guest_user=True
    #         item.save()
        
    #     return render(request, 'messages/thank_you_for_purchased.html', locals())





    
