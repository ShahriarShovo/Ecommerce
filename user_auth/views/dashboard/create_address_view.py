from django.shortcuts import render, redirect
from orders.models.billing_address import BillingAddress
from django.contrib.auth.decorators import login_required
from user_auth.models.user import User



@login_required
def create_address_view(request):
    #TODO 
    user = User.objects.filter(email=request.user)[0]

    # if user.sign_up_platform == 4:
    #     return render(request, 'dashboard/settings.html', locals())
    #     print('-------------------',user)
    # user = request.user
    # email = user.email
    # user_name = user.username
    # first_name=user.first_name
    # last_name=user.last_name
    # print(" User first name --------------", email)
    # try :
    #     address = BillingAddress.objects.get(user=user)
        
    #     zip = address.zipcode
    #     phone = address.phone
    #     house_number = address.house_number
    #     street = address.street
    #     state = address.state
    #     country = address.country
    # except BillingAddress.DoesNotExist:
    #     address = None

    # if request.method == 'POST':
    #     country = request.POST.get('country')
    #     state = request.POST.get('state')
    #     street = request.POST.get('street')
    #     house_number = request.POST.get('building')
    #     phone = request.POST.get('phone')
    #     zip = request.POST.get('zip')

    #     if address:
    #         BillingAddress.objects.update_user_billing_address(
    #                                                            user,
    #                                                            zip,phone,
    #                                                            house_number,
    #                                                            street,
    #                                                            state,
    #                                                            country
    #                                                            )
    #     else:
    #         BillingAddress.objects.create_user_billing_address(
    #                                                             user, 
    #                                                             zip,
    #                                                             phone,
    #                                                             house_number,
    #                                                             street,
    #                                                             state,
    #                                                             country)

    #     return redirect('create_address_view')
    
    # else:
    #     print("If block is not working ")

    return render(request, 'dashboard/settings.html', locals())






   