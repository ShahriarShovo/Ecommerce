from django.shortcuts import redirect
from django.contrib import messages, auth

def user_logout(request):
    auth.logout(request)
    messages.success(request,"Log out successfully")
    return redirect('index')