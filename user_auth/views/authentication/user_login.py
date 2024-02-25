from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from user_auth.models.user import User
from user_auth.models.user_address import User_Address
from django.contrib.auth.decorators import login_required
from user_auth.utiles import detectUser
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

# #later remove
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def user_login(request):
    
    detect = request.POST.get('username_email_phone')
    passowrd = request.POST.get('password')


    # match = User.objects.filter(Q(username = detect)|Q(email = detect)).first()
    # print("match --------------------------",match)

    

    # if match:
    #     email = match.email
    #     print("Email-----------------------", email)
        
    #     user = authenticate(request,email=email, password=passowrd)
        
    #     if user is not None:
    #         login(request,user)

    #         return redirect('myaccount')
        
    #     else:

    #         messages.warning(request,"Email/Username or password is not correct")
    #         return redirect('user_login')
          
    # else:
        
    #     return render(request,'accounts/user_login.html')
    

    
    user = authenticate(request, username=detect, password=passowrd)
    # user = authenticate(request, username=request.POST.get('username_email_phone'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
            # Redirect to a success page.
        return redirect('myaccount')
    
    else:
        

        # if not User.objects.filter(email=detect).exists():
        #     messages.warning(request,'Email not found')
        #     return redirect('user_login')
    
        return render(request,'accounts/user_login.html')
    
    
@login_required(login_url='user_login')
def myaccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)