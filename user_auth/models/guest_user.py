
from django.db import models



class Guest_USer_Saved_data(models.Manager):

    def save_guest_user_data(self, *args, **kwargs):
      
        print("kwargs ---------------",kwargs)
        

        return self.create(first_name=kwargs['first_name'],
                            last_name=kwargs['last_name'],
                              phone=kwargs['phone'],
                                email=kwargs['email'])
    
    # def update_guest_user_data(self,identifier, *args, **kwargs):

    #     try:
    #         user = self.get(identifier=identifier)
    #         print("identifier user ++++++++++++++++++", user)
    #     except:
    #         pass

        



class Guest_User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    objects = Guest_USer_Saved_data()

    def __str__(self) -> str:
        return self.email