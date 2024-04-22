from chat_notification.models import Notification

def  notification_context_processor(request):
    all_notification = Notification.objects.all()

    # print('all notitication----------------', all_notification)

    return {'all_notification': all_notification}
