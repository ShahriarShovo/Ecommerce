from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def order_completed(request):
    user = request.user

    order_completed= Products_Ordered.objects.filter(ordered__user=user,ordered__status='Completed')

    print(" order_completed _____________", order_completed)

    context={
        'order_completed':order_completed
    }

    return render(request,'dashboard_options/order_completed.html',context)