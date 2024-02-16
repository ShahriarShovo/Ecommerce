
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
import uuid
from django.urls import reverse
from products.models.products_model import Products
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered
from products.models.product_variation.size_variant import Product_Size_variant




def generate_payment_id():
    
    #generate transaction id by uuid module
    payment_id=uuid.uuid4()

    #generate transaction id by string and random number
    '''character=string.ascii_letters+string.digits
    transaction_id=''.join(random.choice(character) for i in range(20))'''
    #generate transaction id by only random number 
    #transaction_id = f"{int(time.time())}-{random.randint(10000, 99999)}"

    return payment_id


def generate_oder_id():
    
    #generate transaction id by uuid module
    order_id=uuid.uuid4()

    #generate transaction id by string and random number
    '''character=string.ascii_letters+string.digits
    transaction_id=''.join(random.choice(character) for i in range(20))'''
    #generate transaction id by only random number 
    #transaction_id = f"{int(time.time())}-{random.randint(10000, 99999)}"

    return order_id



def cash_on_delivary_for_single_product(request,pk):

    payment_id=generate_payment_id()
    order_id=generate_oder_id()
    user = request.user

    get_single_product = Products.objects.get(pk=pk)
    product_size = Product_Size_variant.objects.get(pk=request.session['size_pk'])
    p=product_size.pk

    print("get size________", p)
    
    
    
    # print("okay",request.session['product_price'])
    # print(request.session['total_tax'])
    # print(request.session['get_total_all'])

    save_order = Order()
    save_order.user=user
    save_order.order_number=order_id
    save_order.payment_number=payment_id
    save_order.order_total=float(request.session['product_price'])
    save_order.tax=float(request.session['total_tax'])
    save_order.grand_total=float(request.session['get_total_all'])
    save_order.payment_status='Cash_on_delivery'
    save_order.is_ordered=True
    save_order.save()

    Products_Ordered.objects.create(
                ordered=save_order,
                product_name=get_single_product,
                #quantity=items.quantity,
                product_Size_variant=product_size,
                each_product_price=float(request.session['product_price'])
            )
    return HttpResponseRedirect(reverse("invoice", kwargs={'pay_id':payment_id, 'order_id':order_id}))

    
    