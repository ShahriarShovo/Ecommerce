from django.shortcuts import  render, redirect, HttpResponseRedirect, HttpResponse
from orders.models.billing_address import BillingAddress
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from orders.models.orders import Order
from orders.models.product_ordered import Products_Ordered
import uuid
from django.urls import reverse




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
    user = request.user

    if request.user.is_authenticated:
        cart_items= Cart_Item.objects.filter(cart__user=request.user, cart__is_paid=False)
        cart_object = Cart.objects.filter(user=user, is_paid=False)
        get_total= [total.get_cart_total() for total in cart_object]
        get_tax= [tax.get_tax() for tax in cart_object]
        grand_total= [grand_total.get_fully_total() for grand_total in cart_object]

        # print("Cart Total-------------------", get_total)
        # print("Cart get_tax-------------------", get_tax)
        # print("Cart grand_total-------------------", grand_total)

        save_order = Order()
        save_order.user=user
        save_order.order_number=order_id
        save_order.payment_number=payment_id
        save_order.order_total=float(get_total[0])
        save_order.tax=float(get_tax[0])
        save_order.grand_total=float(grand_total[0])
        save_order.payment_status='Cash_on_delivery'
        save_order.is_ordered=True
        save_order.save()

        for items in cart_items:
            Products_Ordered.objects.create(
                ordered=save_order,
                product_name=items.product,
                quantity=items.quantity,
                product_Size_variant=items.product_Size_variant,
                each_product_price=items.get_product_price()
            )
        Cart_Item.objects.filter(cart__user=user).delete()
        return HttpResponseRedirect(reverse("invoice", kwargs={'pay_id':payment_id, 'order_id':order_id}))
    
    else:
        return HttpResponse("Cash on delivery is not working")

