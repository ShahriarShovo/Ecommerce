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
        
        update_user = user_instance.update_user(first_name=first_name,last_name=last_name,username=username,email=email)
        update_user_address = User_Address.objects.update_user_address(user=user_instance, country=country, state=state,street=street,building=building,phone=phone, zip=zip)

    
  
    
        
    context={
        'item_in_carts' : item_in_carts,
        'cart_object' : cart_object,
        'user_address':user_address,
        
    }
    return render(request, 'orders/initial_order.html',context)
        


    # if request.user.is_authenticated:
    #     user = request.user
    #     user_first_name= user.first_name
    #     user_last_name=user.last_name
    #     user_email = user.email
    #     user_name= user.username

    #     try :
    #         address = BillingAddress.objects.get(user=user)
            
    #         zip = address.zipcode
    #         phone = address.phone
    #         house_number = address.house_number
    #         street = address.street
    #         state = address.state
    #         country = address.country
            
    #     except BillingAddress.DoesNotExist:
    #         address = None

    #     if request.method == 'POST':
    #         country = request.POST.get('country')
    #         state = request.POST.get('state')
    #         street = request.POST.get('street')
    #         house_number = request.POST.get('building')
    #         phone = request.POST.get('phone')
    #         zip = request.POST.get('zip')

    #         if address:
    #             BillingAddress.objects.update_user_billing_address(
    #                                                             user,
    #                                                             zip,phone,
    #                                                             house_number,
    #                                                             street,
    #                                                             state,
    #                                                             country
    #                                                             )
    #         else:
    #             BillingAddress.objects.create_user_billing_address(
    #                                                                 user, 
    #                                                                 zip,
    #                                                                 phone,
    #                                                                 house_number,
    #                                                                 street,
    #                                                                 state,
    #                                                                 country)

    #         return redirect('initial_order')


        # # print("Zip code---------------- ", zip_code)
        # carts = Cart.objects.filter(user=request.user, purchased=False)
        # #orders = Order.objects.filter(user=request.user, ordered=False)
        # # if carts.exists() and orders.exists() :
        # #     order = orders[0]
        
        # if carts.exists():
            
        #     total_item_price=request.session['total_item_price']
        #     total_tax=request.session['total_tax'] 
        #     get_total_all=request.session['get_total_all'] 

    # return render(request, 'orders/initial_order.html',context)
        # else:
        #     return redirect("index")
        
    # else:


    #     if request.method == "POST":
    #         first_name = request.POST.get('first_name')
    #         last_name = request.POST.get('last_name')
    #         phone = request.POST.get('phone')
    #         email = request.POST.get('email')

    #         country = request.POST.get('country')
    #         state = request.POST.get('state')
    #         street = request.POST.get('street')
    #         house_number = request.POST.get('building')
    #         phone = request.POST.get('phone')
    #         zip = request.POST.get('zip')

    #         print("First name +++++++++++++++++++++", first_name)
    #         print("last_name name +++++++++++++++++++++", last_name)
    #         print("phone name +++++++++++++++++++++", phone)
    #         print("email name +++++++++++++++++++++", email)


            


    #         guest_user_saved = Guest_User.objects.save_guest_user_data(first_name=first_name,
    #                                                                     last_name=last_name,
    #                                                                     phone=phone,
    #                                                                     email=email)

    #         print( "guest_user_saved+++++++++++++++++++++ ", guest_user_saved)

    #         user = request.user.id

    #         request.session['first_name']=first_name
    #         request.session['last_name']=last_name
    #         request.session['phone']=phone
    #         request.session['email']=email


    #         # identifier = request.session.get('email')
    #         # guest_user_data_update = Guest_User.objects.update_guest_user_data(identifier)

    #         saved_guest_billiging=Guest_BillingAddress.objects.create_user_billing_address(
    #                                                             user=guest_user_saved,
    #                                                             zipcode=zip, phone=phone,
    #                                                             house_number=house_number,
    #                                                             street=street,
    #                                                             state=state,
    #                                                             country=country
    #                                                             )
            
    #         request.session['zipcode']=zip
    #         request.session['phone']=phone
    #         request.session['house_number']=house_number
    #         request.session['street']=street
    #         request.session['state']=state
    #         request.session['country']=country

            


    # carts = Cart.objects.filter(guest_user=True, purchased=False)
    # #orders = Order.objects.filter(user=request.user, ordered=False)
    # # if carts.exists() and orders.exists() :
    # #     order = orders[0]
    # if carts.exists():
    #     total_item_price=request.session['total_item_price']
    #     total_tax=request.session['total_tax'] 
    #     get_total_all=request.session['get_total_all'] 
    #     # print("Session total_item_price ++++++++++++++++++++", total_item_price)
    #     # print("Session total_tax ++++++++++++++++++++", total_tax )
    #     # print("Session get_total_all ++++++++++++++++++++", get_total_all)
    #     return render(request, 'orders/cart_review_guest_user.html', locals())
        
    # else:
    #     return redirect("index")

        

        
        

    
