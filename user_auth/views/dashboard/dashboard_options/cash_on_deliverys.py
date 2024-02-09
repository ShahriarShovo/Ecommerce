from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def cash_on_deliverys(request):
    user = request.user

    cash_on_deliverys= Products_Ordered.objects.filter(ordered__user=user, ordered__payment_status='Cash_on_delivery')

    print(" cash_on_delivery _____________", cash_on_deliverys)

    context={
        'cash_on_deliverys':cash_on_deliverys
    }

    return render(request,'dashboard_options/cash_on_deliverys.html',context)