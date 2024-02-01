from django.shortcuts import render, HttpResponse
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered
from django.shortcuts import get_object_or_404


def invoice(request, pay_id,order_id):
    # print("Pay id ==============", pay_id)
    # print("Pay id ==============", order_id)

    order_instance = Order.objects.get(order_number=order_id, is_ordered=True)
    get_total=order_instance.order_total
    get_tax=order_instance.tax
    get_grand_total = order_instance.grand_total
    # #items_in_order = Products_Ordered.objects.filter(ordered=order_instance).first()
    # #print( " Orderd Product +++++++++++++++++",items_in_order)
    print( " order total  +++++++++++++++++",get_total)
    print( " order get_tax  +++++++++++++++++",get_tax)
    print( " order get_grand_total  +++++++++++++++++",get_grand_total)
    
    # order_instance = Order.objects.filter(payment_number=pay_id, is_ordered=True).first()
    # #order_instance = get_object_or_404(Order, order_number=order_id)
    product_ordered_instances = Products_Ordered.objects.filter(ordered=order_instance)
    print( " Orderd Product +++++++++++++++++",product_ordered_instances)
    # products = [product_ordered.product for product_ordered in order_instance]

    # #product_names = [product_ordered.product.product_name for product_ordered in ordered.all()]
    # print( " Fatch order status +++++++++++++++++",order_instance)
    # product_ordered_instances = Products_Ordered.objects.filter(order=ordered)
    # product_names = [product_ordered.product_name.product_name for product_ordered in product_ordered_instances.all()]
    #print( " Products +++++++++++++++++",product_names)
    # order_details = Order.objects.filter(payment_number=pay_id, is_ordered=True)
    # product= order_details.product
    

    # # # product = fatch_order_details.product.values_list('product_name', flat=True)
    # # # quantity=fatch_order_details.quantity
    
   
    # print( " Fatch order status +++++++++++++++++",product)
    context={
        'fatch_order_details' :product_ordered_instances,
        'order_instance' :order_instance,
        'get_total':get_total,
        'get_tax':get_tax,
        'get_grand_total':get_grand_total,
        'order_number':order_instance
           
        }
    return render(request, 'messages/thank_you_for_purchased.html',context)

   
    
    
    
   
    