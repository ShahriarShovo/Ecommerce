from django.shortcuts import redirect,HttpResponseRedirect, HttpResponse, render,get_object_or_404
from orders.models.orders import Order
from user_auth.models.user import User
from orders.models.billing_address import BillingAddress
from orders.models.guest_billing_address import Guest_BillingAddress
from user_auth.models.guest_user import Guest_User
from products.models.products_model import Products
from user_auth.models.user import User
from user_auth.models.user_address import User_Address, Update_User_Address
from django.contrib import messages
from django.urls import reverse

def buy_now(request, pk):

    get_single_product = Products.objects.get(pk=pk)
    
    product_price = get_single_product.product_price

    total_tax = product_price *(5/100)

    get_total_all= product_price + total_tax

    # request.session['size']
    print("Size in buy Session+++++++++++++++",request.session['size_pk'])

    request.session['product_price']=product_price
    request.session['total_tax']=total_tax
    request.session['get_total_all']=get_total_all
    
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

        user = User.objects.filter(email=request.user)[0]
        user_instance = User.objects.get(email=user)

        if user_instance:
    
            update_user = user_instance.update_user(first_name=first_name,last_name=last_name,username=username,email=email)
            update_user_address = User_Address.objects.update_user_address(user=user_instance, country=country, state=state,street=street,building=building,phone=phone, zip=zip)
            messages.success(request,'Your profile and new address update successfully')
            redirect_url = reverse('buy_now', args=[pk])
            return redirect(redirect_url)
        else:
            messages.warning(request,'somethig is wrong')
            return redirect(redirect_url)


    return render(request, 'orders/buy_now.html',locals())