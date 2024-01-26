from django.shortcuts import  render
from orders.models.billing_address import BillingAddress
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from orders.models.orders import Order
import uuid




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

def cash_on_delivery(request):

    payment_id=generate_payment_id()
    order_id=generate_oder_id()
    # print("Payment Id ===================", payment_id)
    # print("Order Id ===================", order_id)

    if request.user.is_authenticated:
        
        user = request.user
        user_address = BillingAddress.objects.get(user=user)
        cart_items = Cart_Item.objects.filter(cart__user=user)
        cart_object = Cart.objects.get(user=user, is_paid=False)
        print("Cart item +++++++++++++++", cart_items)

        for objects in cart_object:
            objects.is_paid=True
            objects.order_id=order_id
            objects.payment_id=payment_id
            objects.save()

        context={
            'cart_items' : cart_items,
            'total_price_in_cart' :cart_object,
            'payment_id':payment_id,
            'order_id':order_id
        }
        return render(request, 'messages/thank_you_for_purchased.html', context)
        # total_tax=request.session['total_tax'] 
        # total_item_price=request.session['total_item_price']
        # order_object_invoice=cart_items
       
        # order = Order(user=user,
        #               ordered=False,
        #               final_total =total_item_price,
        #               total_tax=total_tax,
        #               sum_of_each_product=total_item_price)
        
        # get_payment_id = Order.objects.filter(paymentId=None,orderId=None,ordered=False)

        # print(" get ++++++++++++ payment Id+++++++++++++",get_payment_id)

        # if len(get_payment_id) == 0 :
        #     order.paymentId=payment_id
        #     order.orderId=order_id
        #     order.ordered=True
        #     order.save()

        # else:
        #     print(" again generate payment Id+++++++++++++")

        # get_payment_id = Order.objects.filter(paymentId=None,orderId=None,ordered=False)
        # print(" get ++++++++++++ payment Id+++++++++++++",get_payment_id)

        # if get_payment_id:
        #     order.paymentId=payment_id
        #     order.orderId=order_id
        #     order.ordered=True
        #     order.save()
        # else:
        #     print(" again generate payment Id+++++++++++++")
        
        # for item in cart_items:
        #     item.purchased = True
        #     item.select_order_stats=1
        #     item.save()
        
    
    else:
        pass

