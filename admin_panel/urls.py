from django.urls import path, include
from .views import admin_home



urlpatterns = [
    path('', admin_home, name='admin_home')
    
]
