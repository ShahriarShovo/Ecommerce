from django.db import models

from django.conf import settings


class Update_User_Address(models.Manager):
    
    def update_user_address(self,user,*args, **kwargs):

        address = self.get(user=user)
        print("Receiving data for user email", address)
        print("Receiving data for user data", kwargs)

        address.country=kwargs['country']
        address.zipcode = kwargs['zip']
        address.phone=kwargs['phone']
        address.house_number=kwargs['building']
        address.street=kwargs['street']
        address.state=kwargs['state']
        address.save()



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

    objects = Update_User_Address()

    def __str__(self) -> str:
        return self.user.email