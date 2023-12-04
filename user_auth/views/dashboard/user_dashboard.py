from django.shortcuts import render, redirect
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order
from cart.models.cart import Cart
from products.models.products_model import Products
import datetime
from django.utils.timezone import now


def user_dashboard(request):

    if request.user.is_authenticated:
        current_user = request.user
        date = datetime.date.today()
        today = now().date()
        #TODO know about 1
        pending_order = Cart.objects.filter(user=current_user,select_order_stats=1)
        print(" order pending -----------", pending_order)  
        #address = BillingAddress.objects.get(user=current_user)
        get_order = Order.objects.filter(user=current_user, ordered=True).order_by('created')
        
        print(" order date -----------",get_order)
    

        return render(request,'dashboard/user_dashboard.html', locals())
        
            
    else:
        return HttpResponse("not login")
    


