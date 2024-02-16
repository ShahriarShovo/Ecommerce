from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from cart.models.cart import Cart
from cart.models.cart_item import Cart_Item
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress
from orders.models.guest_billing_address import Guest_BillingAddress
from user_auth.models.guest_user import Guest_User
from user_auth.models.user import User
from user_auth.models.user_address import User_Address, Update_User_Address
from django.contrib import messages




def initial_order(request):
        
    item_in_carts = Cart_Item.objects.filter(cart__user=request.user, cart__is_paid=False)
    
    cart_object = Cart.objects.get(user=request.user, is_paid=False)

    user = User.objects.filter(email=request.user)[0]
    user_address = User_Address.objects.get(user=user)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
#----------------------------------------------------------
        country = request.POST.get('country')
        state = request.POST.get('state')
        street = request.POST.get('street')
        building = request.POST.get('building')
        phone = request.POST.get('phone')
        zip = request.POST.get('zip')

        user_instance = User.objects.get(email=user)

        if user_instance:
    
            update_user = user_instance.update_user(first_name=first_name,last_name=last_name,username=username,email=email)
            update_user_address = User_Address.objects.update_user_address(user=user_instance, country=country, state=state,street=street,building=building,phone=phone, zip=zip)
            messages.success(request,'Your profile and new address update successfully')
            return redirect('initial_order')
        else:
            messages.warning(request,'somethig is wrong')
            return redirect('initial_order')
  
    context={
        'item_in_carts' : item_in_carts,
        'cart_object' : cart_object,
        'user_address':user_address,
        }
    
    return render(request, 'orders/initial_order.html',context)
        


        

        
        

    
