
from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notify/", consumers.NotificationConsumer.as_asgi()),

    # path('ws/notifications/',consumers.NotificationConsumer.as_asgi()),
]

