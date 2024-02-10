from django.shortcuts import render, HttpResponse
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered
from django.shortcuts import get_object_or_404

from user_auth.models.user import User
from user_auth.models.user_address import User_Address


def invoice(request, pay_id,order_id):
   
    order_instance = Order.objects.get(order_number=order_id, is_ordered=True)
    get_total=order_instance.order_total
    get_tax=order_instance.tax
    get_grand_total = order_instance.grand_total
    product_ordered_instances = Products_Ordered.objects.filter(ordered=order_instance)

    user_address = User_Address.objects.get(user=request.user)
    print("user address____________",user_address)
    
    context={
        'fatch_order_details' :product_ordered_instances,
        'order_instance' :order_instance,
        'get_total':get_total,
        'get_tax':get_tax,
        'get_grand_total':get_grand_total,
        'order_number':order_instance,
        'user_address':user_address,
           
        }
    return render(request, 'messages/thank_you_for_purchased.html',context)

   
    
    
    
   
    