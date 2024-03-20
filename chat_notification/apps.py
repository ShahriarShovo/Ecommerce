from django.apps import AppConfig


class ChatNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat_notification'

    # 1. 👇 Add this line for signals
    def ready(self):
        import chat_notification.signals
