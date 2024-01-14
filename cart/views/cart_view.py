from django.shortcuts import render,redirect, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order



def cart_view(request):

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, purchased=False)

        if carts.exists():

            total_item_price_store_in_array =[]
            total_item_price =0
            
            for items in carts:
                #totals = items.quantity * items.item.product_price
                totals = items.quantity * items.price
                total_item_price_store_in_array.append(totals)

            for sum_of_total_item_price in total_item_price_store_in_array:
                total_item_price +=sum_of_total_item_price

            total_tax = total_item_price *(5/100)
            get_total_all = total_item_price + total_tax

            coupon_code = request.POST.get('coupon_code')
            print("coupon_code--------------",coupon_code)

            request.session['total_item_price'] = total_item_price
            request.session['total_tax'] = total_tax
            request.session['get_total_all'] = get_total_all

            # print("Session ++++++++++++++++++++", request.session['total_item_price'])
            
            return render(request, 'cart/cart.html', locals())
        
        else:
            return redirect("index")
        
        
    else:

        carts = Cart.objects.filter(guest_user=True, purchased=False)
        if carts.exists():
            total_item_price_store_in_array =[]
            total_item_price =0
            
            for items in carts:
                totals = items.quantity * items.item.product_price
                total_item_price_store_in_array.append(totals)

            for sum_of_total_item_price in total_item_price_store_in_array:
                total_item_price +=sum_of_total_item_price

            total_tax = total_item_price *(5/100)
            get_total_all = total_item_price + total_tax

            request.session['total_item_price'] = total_item_price
            request.session['total_tax'] = total_tax
            request.session['get_total_all'] = get_total_all

            # print("Session ++++++++++++++++++++", request.session['total_item_price'])
            
            return render(request, 'cart/cart.html', locals())
        
        else:
            return redirect("index")

