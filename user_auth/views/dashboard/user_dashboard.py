from django.shortcuts import render, redirect
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order
from cart.models.cart import Cart
from products.models.products_model import Products
import datetime
from django.utils.timezone import now
from user_auth.models.user_address import User_Address
from orders.models.product_ordered import Products_Ordered
from django.db.models import Sum


# def get_client_ip(request):
#     # Get the user's IP address from the request
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#         print("user Ip________",ip)
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#         print("server Ip________",ip)
#     return ip

PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )

def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip


def user_dashboard(request):

    if request.user.is_authenticated:
        current_user = request.user
        date = datetime.date.today()
        today = now().date()
        user_address = User_Address.objects.get(user=current_user)
        
        total_orders = Products_Ordered.objects.filter(ordered__user=current_user, ordered__is_ordered=True).count()
        pending_count = Order.objects.filter(status='Pending').count()
        completed_count = Order.objects.filter(status='Completed').count()

        payment_status = Order.objects.filter(payment_status='Cash_on_delivery').count()
        paid_status = Order.objects.filter(payment_status='Paid').count()

        grand_total_amount = Order.objects.aggregate(grand_total_amount=Sum('grand_total'))['grand_total_amount']
        tax = Order.objects.aggregate(tax=Sum('tax'))['tax']
        order_total=Order.objects.aggregate(order_total=Sum('order_total'))['order_total']

        #print("user total___________",grand_total_amount)


        ip_address = ip_address = get_client_ip(request)

        print("ip_address___________",ip_address)

       
    

        return render(request,'dashboard/user_dashboard.html', locals())
        
            
    else:
        return HttpResponse("not login")
    


