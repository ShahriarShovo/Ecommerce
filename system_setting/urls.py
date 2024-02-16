from django.urls import path, include
from system_setting.views.contact_and_details import contact_and_details


urlpatterns = [
    path('', contact_and_details, name='contact_and_details'),
]
