from django.shortcuts import render, redirect, HttpResponse
from user_auth.models.user import User
from django.contrib.auth.decorators import login_required
from user_auth.utiles import detectUser
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.contrib import messages


def user_login(request):
    
    detect = request.POST.get('username_email_phone')
    passowrd = request.POST.get('password')

    print("User name --------------------------",detect)
    print("Password --------------------------",passowrd)
        
    match = User.objects.filter(Q(username = detect)|Q(email = detect)).first()
    print("match --------------------------",match)

    if match:
        email = match.email
        print("Email-----------------------", email)
        user = authenticate(request,email=email, password=passowrd)
        
        if user is not None:
            login(request,user)

            return redirect('index')
        
        else:

            messages.warning(request,"Email/Username or password is not correct")
            return redirect('user_login')
          
    else:
        
        return render(request,'accounts/user_login.html')
    
    
@login_required(login_url='user_login')
def myaccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)