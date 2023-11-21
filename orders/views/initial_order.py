from django.shortcuts import render,redirect,get_object_or_404
from cart.models.cart import Cart
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress



def initial_order(request):
    user = request.user
    user_first_name= user.first_name
    user_last_name=user.last_name
    user_email = user.email
    user_name= user.username
    # #user_billing_address = BillingAddress.objects.get(user=user)
    # user_billing_address=get_object_or_404(BillingAddress, user=user)

    # #if request.POST.get('delivery_info_update'):

    
    # zip_code=user_billing_address.zipcode
    # phone =user_billing_address.phone
    # house_number=user_billing_address.house_number
    # street=user_billing_address.street
    # state=user_billing_address.state
    # country=user_billing_address.country

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
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists() :
        order = orders[0]
        return render(request, 'orders/initial_order.html', locals())
    else:
        return redirect("index")

    
