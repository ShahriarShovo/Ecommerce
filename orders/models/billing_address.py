from django.db import models
from django.conf import settings
from user_auth.models.guest_user import Guest_User

# Create your models here.

class Billing_Address_Update_Manager(models.Manager):

    # def create_user_billing_address(self, user, new_zipcode, new_phone,new_house_number,new_street,new_state,new_country):
    #     return self.create(user=user, zipcode=new_zipcode,
    #                         phone=new_phone, house_number=new_house_number,
    #                         street=new_street,state=new_state,
    #                          country= new_country)

    # def update_user_billing_address(self, user, new_zipcode, new_phone,new_house_number,new_street,new_state,new_country):
    #     address = self.get(user=user)
    #     address.zipcode=new_zipcode
    #     address.phone=new_phone
    #     address.house_number=new_house_number
    #     address.street=new_street
    #     address.state=new_state,
    #     address.country= new_country
    #     address.save()


    
    def create_user_billing_address(self, user, *args, **kwargs):

        print("User ---------------",user)
        print("args ---------------",args)
        print("kwargs ---------------",kwargs)

        return self.create(user=user, zipcode=args[0],
                            phone=args[1], house_number=args[2],
                            street=args[3],state=args[4],
                             country= args[5])
    
    def update_user_billing_address(self, user, *args, **kwargs):
        address = self.get(user=user)
        address.zipcode=args[0]
        address.phone=args[1]
        address.house_number=args[2]
        address.street=args[3]
        address.state=args[4]
        address.country= args[5]
        address.save()
    


class BillingAddress(models.Model):

    BANGLADESH=1
    COUNTRY_CHOOSED  = ((BANGLADESH, 'Bangladesh'), )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    guest_user = models.ForeignKey(Guest_User, on_delete=models.CASCADE, null=True, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    house_number = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    country    = models.PositiveSmallIntegerField(choices=COUNTRY_CHOOSED, blank=True, null=True)
    guest_user = models.BooleanField(default=False)

    objects = Billing_Address_Update_Manager()
    
    def __str__(self):
        return self.phone