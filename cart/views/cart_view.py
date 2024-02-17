from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from orders.models.orders import Order
from products.models.products_model import Coupon_Code
from django.contrib import messages


def cart_view(request):

    #carts = Cart.objects.filter(user=request.user, is_paid=False)
    item_in_carts = Cart_Item.objects.filter(cart__user=request.user, cart__is_paid=False)
   
    cart_object = Cart.objects.get(user=request.user, is_paid=False)

    cart_item_count = item_in_carts.count()

    #print('=============count', cart_item_count)
    # total= cart_object.get_cart_total()
    # tax = cart_object.get_tax()
    # final_total = total + tax

    # get_code = request.GET.get('coupon_code')
    # print ("Coupon code caputure +++++++++++++++++++++",get_code)

    if request.method == "POST":
        get_code = request.POST.get('coupon_code')
        #print ("Coupon code caputure +++++++++++++++++++++",get_code)
        coupon_object = Coupon_Code.objects.filter(code__icontains=get_code)

        print("get money_______", coupon_object[0].discount)

       
        if not coupon_object.exists():
            messages.info(request,'This is not valid coupon')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif cart_object.coupon:
            messages.warning(request,'Coupon already applied')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:

            if cart_object.get_cart_total() < coupon_object[0].minimum_amount:
                messages.info(request,f"Please buy more than {coupon_object[0].minimum_amount}")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            elif coupon_object[0].is_expired_coupon_code:
                messages.warning(request,'Coupon exired')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            else:
                cart_object.coupon=coupon_object[0]
                # if coupon_object[0].is_expired_coupon_code==False :
                #     coupon_object[0].is_expired_coupon_code=True
                #     coupon_object[0].save()
                cart_object.save()
                messages.success(request,f"Coupon applied succesfully and get {coupon_object[0].discount} discount.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context={
        'carts':item_in_carts,
        'cart_object':cart_object,
        #'final_total':final_total,
        'cart_item_count':cart_item_count,
        
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

