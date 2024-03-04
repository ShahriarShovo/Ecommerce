from django.shortcuts import render
from orders.models.orders import Order



def order_details_status(request):
    

    if request.user.is_authenticated:

        orders_with_products = Order.objects.prefetch_related('product_order')

        context={
                'orders_with_products':orders_with_products,
            }

        # print(" all odered _____________", orders_with_products)

        # if orders_with_products.exists():

        #     for order in orders_with_products:
        #         print("Order Number:", order.order_number)
        #         print("Order status:", order.status)
        #         print("Products Ordered:")
        #         for product in order.product_order.all():
        #             print("- ", product.product_name)
        #             print("- ", product.quantity)
        #             print("- ", product.product_Size_variant)
        #             print("- ", product.each_product_price)
                    
            

        # else:
        #     orders_with_products = None

        return render(request,'dashboard_options/order_details_status.html',context)