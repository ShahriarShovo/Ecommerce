
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def deactivate_account(request):
    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        messages.success(request, 'Your account has been deactivated.')
        return redirect('user_logout')  # Redirect to logout page after deactivation
    #return render(request, 'deactivate_account.html')