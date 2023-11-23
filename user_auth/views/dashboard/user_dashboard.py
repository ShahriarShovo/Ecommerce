from django.shortcuts import render, redirect
from django.http import HttpResponse
from orders.models.billing_address import BillingAddress
from orders.models.orders import Order
from cart.models.cart import Cart
from products.models.models import Products
from datetime import datetime


def user_dashboard(request):

    if request.user.is_authenticated:



        current_user = request.user
       
           
        #address = BillingAddress.objects.get(user=current_user)
        # order_completed = Order.objects.filter(ordered=True, select_order_stats=1).values()
        # qss = order_completed[0]
        # last_orderd= qss.created

        #print(" order complete-----------", last_orderd)

        #pending_products = Products.objects.filter(cart__order__ordered=True, cart__order__select_order_stats=1,cart__order__created=datetime.today())
        # pending_products = Products.objects.filter(cart__order__ordered=True, 
        #                                            cart__order__select_order_stats=1)
            #order_completed_qs=order_completed[0]
            # id = order_completed_qs.id
            #name = order_completed.orderItems
        pending_order = Order.objects.filter(user=current_user, ordered=True, select_order_stats=1).values()

            
           
        print(" order ----------complete-----------", pending_order)

        return render(request,'dashboard/user_dashboard.html', locals())
        
            
    else:
        return HttpResponse("not login")
    


