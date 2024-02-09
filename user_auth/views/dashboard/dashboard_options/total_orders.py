from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def total_orders(request):
    user = request.user
    
    
    get_ordered= Products_Ordered.objects.filter(ordered__user=user,ordered__is_ordered=True)

    #print(" all odered _____________", get_ordered)

    context={
        'get_all_ordered':get_ordered
    }

    return render(request,'dashboard_options/total_orders.html',context)