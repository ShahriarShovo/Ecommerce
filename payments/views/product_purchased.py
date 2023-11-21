from orders.models.orders import Order
from cart.models.cart import Cart
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress


def product_purchased(request,val_id, tran_id):

    print("Val_id-----------------",val_id)
    print("tran_id-----------------",tran_id)
    user = request.user

    order_qs = Order.objects.filter(user=user, ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.select_order_stats=1
    order.save()
    cart_items = Cart.objects.filter(user=user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()
    return HttpResponseRedirect(reverse('order_view'))
    #return render(request, 'messages/thank_you_for_purchased.html', locals())
    #return render(request, "message/thank_you.html")

import datetime

def order_view(request):
    try:
        now=datetime.datetime.now()
        print("Date: "+ now.strftime("%Y-%m-%d"))
        user = request.user
        user_address = BillingAddress.objects.get(user=user)
        street = user_address.street
        state = user_address.state
        zip_code = user_address.zipcode
        country = user_address.country
        orders = Order.objects.filter(user=request.user, ordered=True, select_order_stats=1).values()
        # orderId=orders.orderId
        # paymentId=orders.paymentId
        # o= orders.select_order_stats
        # print("Orders- -----------", o)

        context = {"orders": orders}
        return render(request, 'messages/thank_you_for_purchased.html',locals())
    except:

        return HttpResponse("No order")
    