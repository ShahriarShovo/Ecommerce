
from django.urls import re_path,path
from chat_notification.consumers.notification import NotificationConsumer

websocket_urlpatterns = [
    # re_path(r"ws/notify/", consumers.NotificationConsumer.as_asgi()),

    path('ws/notify/',NotificationConsumer.as_asgi()),
]

