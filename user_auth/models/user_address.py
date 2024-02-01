from django.db import models

from django.conf import settings


class User_Address(models.Model):
    

    BANGLADESH=1
    COUNTRY_CHOOSED  = ((BANGLADESH, 'Bangladesh'), )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    zipcode = models.CharField(max_length=10, blank=True,null=True)
    phone = models.CharField(max_length=200, blank=True,null=True)
    house_number = models.CharField(max_length=20, blank=True,null=True)
    street = models.CharField(max_length=30, blank=True,null=True)
    state = models.CharField(max_length=30, blank=True,null=True)
    country    = models.PositiveSmallIntegerField(choices=COUNTRY_CHOOSED, blank=True, null=True)
    #guest_user = models.BooleanField(default=False)