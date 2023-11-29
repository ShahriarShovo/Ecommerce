
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order


def invoice(request):
    try:
        now=datetime.datetime.now()
        print("Date: "+ now.strftime("%Y-%m-%d"))
        user = request.user
        user_address = BillingAddress.objects.get(user=user)
        street = user_address.street
        state = user_address.state
        zip_code = user_address.zipcode
        country = user_address.country
        print("Country ------------------------", country)
        orders = Order.objects.filter(user=request.user, ordered=True, select_order_stats=1).values()
        current_oders = orders[0]
        
        print("Objects ------------------", orders)
        return render(request, 'messages/thank_you_for_purchased.html', locals())
    
    except:
        return HttpResponse("No order")



