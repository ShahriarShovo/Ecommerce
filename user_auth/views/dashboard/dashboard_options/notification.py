from django.shortcuts import render
from chat_notification.models import Notification


def notification(request):
    notifications = Notification.objects.all()
    context={
        'notifications':notifications,
    }
    return render(request, 'dashboard/notification.html', context)