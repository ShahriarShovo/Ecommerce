from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def change_password(request):

    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            print(" Pasword not change")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user=request.user
            user.set_password(new_password)
            user.save()
            print(" Pasword change")

            user = authenticate(email=user.email, password=new_password)
            if user is not None:
                login(request, user)
            return redirect('user_dashboard')

    return render(request,'accounts/change_password.html')