# from django.shortcuts import render, get_object_or_404, redirect
# from user_auth.models.user import User
# from orders.models.billing_address import BillingAddress
# from django.contrib.auth.decorators import login_required



# def update_address_view(request,pk):
#     user=request.user.pk
#     current_user_address=get_object_or_404(BillingAddress, user=user)
#     print("Current User Id ----------------- ", user)
#     print("Current User address ----------------- ", current_user_address)
#     zip = current_user_address.zipcode
#     phone = current_user_address.phone
#     house_number = current_user_address.house_number
#     street = current_user_address.street
#     state = current_user_address.state
#     country = current_user_address.country
#     print("Current User zip ----------------- ", zip)
#     print("Current User phone ----------------- ", phone)
#     print("Current User house_number ----------------- ", house_number)
#     print("Current User street ----------------- ", street)
#     print("Current User state ----------------- ", state)
#     print("Current User country ----------------- ", country)

#     context={
#             # 'user_first_name' :user_first_name,
#             # 'user_last_name' : user_last_name,
#             # 'user_name' : user_name,
#             # 'user_email' : user_email,

#             'zip':zip,
#             'phone' :phone,
#             'house_number' :house_number,
#             'street':street,
#             'state':state,
#             'country' :country,
#         }
#     return render(request, 'dashboard/settings.html', context=context)


  



# # @login_required
# # def settings(request):
# #     user = request.user
# #     user_first_name= user.first_name
# #     user_last_name=user.last_name
# #     user_email = user.email
# #     user_name= user.username

# #     #current_user_address= BillingAddress.objects.get(user=user)
# #     current_user_address=get_object_or_404(BillingAddress, user=user)
# #     zip = current_user_address.zipcode
# #     phone = current_user_address.phone
# #     house_number = current_user_address.house_number
# #     street = current_user_address.street
# #     state = current_user_address.state
# #     country = current_user_address.country

# #     if request.method == "POST":
# #         if 'create_address_view' in request.POST:
# #         #instance = get_object_or_404(BillingAddress, user=user)
# #             if request.POST.get('country'):
# #                 BillingAddress.custom_manager.update_country(user, request.POST.get('country'))
# #             if request.POST.get('phone'):
# #                 BillingAddress.custom_manager.update_phone(user, request.POST.get('phone'))
# #             if request.POST.get('street'):
# #                 BillingAddress.custom_manager.update_street(user, request.POST.get('street'))
# #             if request.POST.get('state'):
# #                 BillingAddress.custom_manager.update_state(user, request.POST.get('state'))
# #             if request.POST.get('building'):
# #                 BillingAddress.custom_manager.update_house_number(user, request.POST.get('building'))
# #             if request.POST.get('zip'):
# #                 BillingAddress.custom_manager.update_zipcode(user, request.POST.get('zip'))

# #         elif 'user_final_checkout_form' in request.POST:
# #         #instance = get_object_or_404(BillingAddress, user=user)
# #             if request.POST.get('country'):
# #                 BillingAddress.custom_manager.update_country(user, request.POST.get('country'))
# #             if request.POST.get('phone'):
# #                 BillingAddress.custom_manager.update_phone(user, request.POST.get('phone'))
# #             if request.POST.get('street'):
# #                 BillingAddress.custom_manager.update_street(user, request.POST.get('street'))
# #             if request.POST.get('state'):
# #                 BillingAddress.custom_manager.update_state(user, request.POST.get('state'))
# #             if request.POST.get('building'):
# #                 BillingAddress.custom_manager.update_house_number(user, request.POST.get('building'))
# #             if request.POST.get('zip'):
# #                 BillingAddress.custom_manager.update_zipcode(user, request.POST.get('zip'))
        
    

# #     context={
# #             'user_first_name' :user_first_name,
# #             'user_last_name' : user_last_name,
# #             'user_name' : user_name,
# #             'user_email' : user_email,

# #             'zip':zip,
# #             'phone' :phone,
# #             'house_number' :house_number,
# #             'street':street,
# #             'state':state,
# #             'country' :country,
# #         }
# #     return render(request, 'dashboard/settings.html', context=context)
