from django.shortcuts import render,redirect, HttpResponse
from cart.models.cart import Cart,Cart_Item
from orders.models.orders import Order
from django.shortcuts import get_object_or_404


def cart_view(request):

    #carts = Cart.objects.filter(user=request.user, is_paid=False)
    item_in_carts = Cart_Item.objects.filter(cart__user=request.user, cart__is_paid=False)
    total_price_in_cart = Cart.objects.get(user=request.user, is_paid=False)

    total= total_price_in_cart.get_cart_total()
    tax = total_price_in_cart.get_tax()
    final_total = total + tax
   
    context={
        'carts':item_in_carts,
        'total_price_in_cart':total_price_in_cart,
        'final_total':final_total
    }
    return render(request, 'cart/cart.html', context=context)


# def cart_view(request):

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, purchased=False)

#         if carts.exists():

#             total_item_price_store_in_array =[]
#             total_item_price =0
            
#             for items in carts:
#                 #totals = items.quantity * items.item.product_price
#                 totals = items.quantity * items.price
#                 total_item_price_store_in_array.append(totals)

#             for sum_of_total_item_price in total_item_price_store_in_array:
#                 total_item_price +=sum_of_total_item_price

#             total_tax = total_item_price *(5/100)
#             get_total_all = total_item_price + total_tax

#             if request.method=='POST':
#                 coupon_code = request.POST.get('coupon_code')
#                 print("coupon_code--------------",coupon_code)

#             request.session['total_item_price'] = total_item_price
#             request.session['total_tax'] = total_tax
#             request.session['get_total_all'] = get_total_all

#             # print("Session ++++++++++++++++++++", request.session['total_item_price'])
            
#             return render(request, 'cart/cart.html', locals())
        
#         else:
#             return redirect("index")
        
        
#     else:

#         carts = Cart.objects.filter(guest_user=True, purchased=False)
#         if carts.exists():
#             total_item_price_store_in_array =[]
#             total_item_price =0
            
#             for items in carts:
#                 totals = items.quantity * items.item.product_price
#                 total_item_price_store_in_array.append(totals)

#             for sum_of_total_item_price in total_item_price_store_in_array:
#                 total_item_price +=sum_of_total_item_price

#             total_tax = total_item_price *(5/100)
#             get_total_all = total_item_price + total_tax

#             request.session['total_item_price'] = total_item_price
#             request.session['total_tax'] = total_tax
#             request.session['get_total_all'] = get_total_all

#             # print("Session ++++++++++++++++++++", request.session['total_item_price'])
            
#             return render(request, 'cart/cart.html', locals())
        
#         else:
#             return redirect("index")

