from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered
from django.contrib import messages


def track_orders(request):

    if request.method=="POST":
        get_order_id = request.POST.get('order_id')
        #print("Track order ----------", get_order_id)

        get_product_info = Products_Ordered.objects.filter(ordered__order_number=get_order_id)
        get_order_status = Order.objects.filter(order_number=get_order_id).first()
        
        #print("Track order ----------", get_order_status)
        if get_product_info:

            context={
                'get_product_info':get_product_info,
                'get_order_status' :get_order_status,
            }

            return render(request, 'orders/track_order_result.html', context)
        else:
            messages.info(request, 'Order Not Found')

    return render(request, 'orders/track_orders.html')