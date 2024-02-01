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
        #order_id = Order.objects.get(user=user, is_ordered=False)
        #get_product_price= [price.get_product_price() for price in cart_items]
        cart_object = Cart.objects.filter(user=user, is_paid=False)
        # product_name= [product_name.product.pk  for product_name in cart_items.all()]
        # product_size= [size.product_Size_variant  for size in cart_items.all()]
        get_total= [total.get_cart_total() for total in cart_object]
        get_tax= [tax.get_tax() for tax in cart_object]
        grand_total= [grand_total.get_fully_total() for grand_total in cart_object]

        print("Cart Total-------------------", get_total)
        print("Cart get_tax-------------------", get_tax)
        print("Cart grand_total-------------------", grand_total)

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
                each_product_price=items.get_product_price()
            )
        #print("get_product_price-------------------", get_product_price)
        #print("Product size-------------------", product_size)
        #print("Product id-------------------", product_name)

        # for items in cart_items:
         
        #     save_item = Order()
        #     save_item.user=user
        #     save_item.payment_number=payment_id
        #     save_item.order_number=order_id
        #     save_item.order_total=float(get_total[0])
        #     save_item.tax=float(get_tax[0])
        #     save_item.grand_total=float(grand_total[0])
        #     save_item.payment_status='Cash_on_delivery'
        #     save_item.is_ordered=True
        #     save_item.product=cart_items.product
           
        #     # save_item.quantity=items.quantity
        #     # save_item.each_product_price=items.get_product_price()
        #     #save_item.product=items.product.pk
        #     #save_item.product_Size_variant=product_size[0]
        #     save_item.save()

            # cart_item = Cart_Item.objects.get(pk=items.pk)
            # products = cart_item.product.all()
            # save_item = Order.objects.get(pk=save_item.pk)
            # save_item.product.set(products)
            #save_item.product_Size_variant.set(product_size)
            # product = cart_item.product.all()
            # product_s_variation = cart_item.product_Size_variant.all()
            # save_item.product.set(items.product)
            # save_item.product_Size_variant.set(items.product_s_variation)
            # save_item.save()


        Cart_Item.objects.filter(cart__user=user).delete()
        return HttpResponseRedirect(reverse("invoice", kwargs={'pay_id':payment_id, 'order_id':order_id}))
    else:
        return HttpResponse("Cash on delivery is not working")

    #return render(request, 'messages/thank_you_for_purchased.html')

    # payment_id=generate_payment_id()
    # order_id=generate_oder_id()
   
    # if request.user.is_authenticated:
        
    #     user = request.user
    #     user_address = BillingAddress.objects.get(user=user)
    #     cart_items = Cart_Item.objects.filter(cart__user=user)
    #     quantities = [quantities.quantity  for quantities in cart_items.all()]
    #     product_name= [product_name.product  for product_name in cart_items.all()]
    #     print("Total quantity-------------------", product_name)
    #     cart_object = Cart.objects.filter(user=user, is_paid=False)
    #     get_total= [total.get_cart_total() for total in cart_object]
    #     get_tax= [tax.get_tax() for tax in cart_object]
    #     grand_total= [grand_total.get_fully_total() for grand_total in cart_object]
    #     print("Cart Total-------------------", get_total)
    #     print("Cart get_tax-------------------", get_tax)
    #     print("Cart grand_total-------------------", grand_total)
        

        

    #     for objects in cart_object:
    #         objects.is_paid=True
    #         objects.order_id=order_id
    #         objects.payment_id=payment_id
    #         objects.quantity=quantities
    #         objects.total=get_total
    #         objects.tax=get_tax
    #         objects.grand_total=grand_total
    #         objects.products.set(product_name)
    #         objects.save()
        
    #     context={
    #         'cart_items' : cart_items,
    #         'total_price_in_cart' :cart_object,
    #         'payment_id':payment_id,
    #         'order_id':order_id,
            
    #     }

    #     #clear_cart_item = cart_items.delete()

    
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
        
    
    # else:
    #     pass

