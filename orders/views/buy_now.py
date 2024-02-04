from django.shortcuts import redirect,HttpResponseRedirect, HttpResponse, render,get_object_or_404
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress
from orders.models.guest_billing_address import Guest_BillingAddress
from user_auth.models.guest_user import Guest_User
from products.models.products_model import Products

def buy_now(request, pk):

    get_single_product = Products.objects.get(pk=pk)
    product_name = get_single_product.product_name
    product_brand = get_single_product.product_brand
    product_imag = get_single_product.product_image
    product_price = get_single_product.product_price

    total_tax = product_price *(5/100)

    get_total_all= product_price + total_tax
    
    print("Single Product ----------------------", get_single_product)

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


        return render(request, 'orders/buy_now.html',locals())