from orders.models.orders import Order
from cart.models.cart import Cart
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress




def product_purchased(request,val_id, tran_id):

    arry =[]

    user = request.user
    cart_items = Cart.objects.filter(user=user, purchased=False)
    get_items = cart_items[0]
    total_quantity=get_items.quantity
    total_products = get_items.item
    arry.append(total_products)
   
    print("total_products --------------------",arry)

    for item in cart_items:
        item.purchased = True
        item.save()

    order_qs = Order.objects.filter(user=user, ordered=False)
    order = order_qs[0]
    p = order.orderItems
    print("Order Qs --------------------", p)
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    order.paymentId = val_id
    order.select_order_stats=1
    order.quantity = total_quantity
    #order.product= total_products
    order.save()

    return HttpResponseRedirect(reverse('invoice'))




    
