from django.contrib import admin

# Register your models here.
from .models import Notification

# 👇 2. Add this line to add the notification
admin.site.register(Notification)
