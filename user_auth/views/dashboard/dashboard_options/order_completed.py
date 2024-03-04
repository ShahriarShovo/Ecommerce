from django.shortcuts import render
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered


def order_completed(request):
    
    if request.user.is_authenticated:

        orders_with_products = Order.objects.prefetch_related('product_order')

        print(" all odered _____________", orders_with_products)

        for order in orders_with_products:
            print("Order Number_________:", order.order_number)
            print("Order status________--:", order.status)
            print("Products Ordered_______:")
            for product in order.product_order.all():
                print("- ", product.product_name)
                print("- ", product.quantity)
                print("- ", product.product_Size_variant)
                print("- ", product.each_product_price)
                
        context={
            # 'orders_with_products':orders_with_products,
        }

    return render(request,'dashboard_options/order_completed.html',context)