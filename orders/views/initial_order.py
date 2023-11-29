from django.shortcuts import render,redirect,get_object_or_404
from cart.models.cart import Cart
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress
from user_auth.models.guest_user import Guest_User



def initial_order(request):

    if request.user.is_authenticated:
        user = request.user
        user_first_name= user.first_name
        user_last_name=user.last_name
        user_email = user.email
        user_name= user.username
        try :
            address = BillingAddress.objects.get(user=user)
            
            zip = address.zipcode
            phone = address.phone
            house_number = address.house_number
            street = address.street
            state = address.state
            country = address.country
            
        except BillingAddress.DoesNotExist:
            address = None

        if request.method == 'POST':
            country = request.POST.get('country')
            state = request.POST.get('state')
            street = request.POST.get('street')
            house_number = request.POST.get('building')
            phone = request.POST.get('phone')
            zip = request.POST.get('zip')

            if address:
                BillingAddress.objects.update_user_billing_address(
                                                                user,
                                                                zip,phone,
                                                                house_number,
                                                                street,
                                                                state,
                                                                country
                                                                )
            else:
                BillingAddress.objects.create_user_billing_address(
                                                                    user, 
                                                                    zip,
                                                                    phone,
                                                                    house_number,
                                                                    street,
                                                                    state,
                                                                    country)

            return redirect('initial_order')


        # print("Zip code---------------- ", zip_code)
        carts = Cart.objects.filter(user=request.user, purchased=False)
        #orders = Order.objects.filter(user=request.user, ordered=False)
        # if carts.exists() and orders.exists() :
        #     order = orders[0]
        
        if carts.exists():
            
            total_item_price=request.session['total_item_price']
            total_tax=request.session['total_tax'] 
            get_total_all=request.session['get_total_all'] 

            return render(request, 'orders/initial_order.html', locals())
        else:
            return redirect("index")
        
    else:

        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')


            guest_user_saved = Guest_User(first_name=first_name,last_name=last_name,phone=phone,email=email)
            guest_user_saved.save()

            retrive_guest_user=Guest_User.objects.filter(email=email)[0]
            g_f_name=retrive_guest_user.first_name
            g_l_name=retrive_guest_user.last_name
            g_phone=retrive_guest_user.phone
            g_email=retrive_guest_user.email


            
            country = request.POST.get('country')
            state = request.POST.get('state')
            street = request.POST.get('street')
            house_number = request.POST.get('building')
            phone = request.POST.get('phone')
            zip = request.POST.get('zip')

            guest_billing_address = BillingAddress(zipcode=zip,phone=phone,house_number=house_number,
                                                   street=street,state=state,country=country,guest_user=True)
            guest_billing_address.save()

            g_country=retrive_guest_billing_address=BillingAddress.objects.filter(phone=phone)[0]
            g_state=retrive_guest_billing_address.country
            g_street=retrive_guest_billing_address.state
            g_house_number=retrive_guest_billing_address.street
            g_phone=retrive_guest_billing_address.phone
            g_zip=retrive_guest_billing_address.zipcode


            print(" Guest user phone ++++++++++++++++++++++",retrive_guest_billing_address)





            

            # g_country=request.session['country']
            # g_state=request.session['state']
            # g_street =request.session['street']
            # g_house_number =request.session['house_number']
            # g_phone=request.session['phone']
            # g_zip=request.session['zip']

            # print("country ___________-name ", country)
            # print("state ___________-name ", state)
            # print("street ___________-name ", street)
            # print("house_number ___________-name ", house_number)
            # print("phone ___________-name ", phone)
            # print("zip ___________-name ", zip)

        carts = Cart.objects.filter(guest_user=True, purchased=False)
        #orders = Order.objects.filter(user=request.user, ordered=False)
        # if carts.exists() and orders.exists() :
        #     order = orders[0]
        if carts.exists():
            total_item_price=request.session['total_item_price']
            total_tax=request.session['total_tax'] 
            get_total_all=request.session['get_total_all'] 
            # print("Session total_item_price ++++++++++++++++++++", total_item_price)
            # print("Session total_tax ++++++++++++++++++++", total_tax )
            # print("Session get_total_all ++++++++++++++++++++", get_total_all)
            return render(request, 'orders/cart_review_guest_user.html', locals())
            
        else:
            return redirect("index")

        
        

    
