from django.shortcuts import render, redirect
from orders.models.billing_address import BillingAddress
from django.contrib.auth.decorators import login_required
from user_auth.models.user import User
from user_auth.models.user_address import User_Address, Update_User_Address



@login_required
def update_address(request):

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

    return render(request, 'dashboard/settings.html', locals())






   