from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def pending_orders(request):
    user = request.user

    pending_ordered= Products_Ordered.objects.filter(ordered__user=user,ordered__status='Pending')

    print(" all odered _____________", pending_ordered)

    context={
        'pending_all_ordered':pending_ordered
    }

    return render(request,'dashboard_options/pending_orders.html',context)