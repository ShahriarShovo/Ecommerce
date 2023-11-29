from django.shortcuts import redirect, render
from user_auth.models.user import User

def fatch_user(request):

    fatch_all_user = User.objects.all()

    context={
        'users' :fatch_all_user
    }
    return render(request, 'admin/dashboard/user/fatch_user.html', context=context)