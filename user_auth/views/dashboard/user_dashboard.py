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

       
    

        return render(request,'dashboard/user_dashboard.html', locals())
        
            
    else:
        return HttpResponse("not login")
    


