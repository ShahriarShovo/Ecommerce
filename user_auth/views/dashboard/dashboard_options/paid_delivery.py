from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def paid_delivery(request):
    user = request.user

    paid_delivery= Products_Ordered.objects.filter(ordered__user=user, ordered__payment_status='Paid')

    print(" paid_delivery _____________", paid_delivery)

    context={
        'paid_delivery':paid_delivery
    }

    return render(request,'dashboard_options/paid_delivery.html',context)