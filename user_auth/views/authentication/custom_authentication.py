from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from user_auth.models.user_address import User_Address
# from user_auth.models.user import User
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib import messages

class CustomAuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        User = get_user_model()
        try:
            
            # Check if username is an email
            user = User.objects.get(email=username)

        except User.DoesNotExist:

            try:
                # Check if username is a username
                user = User.objects.get(username=username)
                
            except User.DoesNotExist:

                return None
                # Check if username is a phone number
                #user = User.objects.get(phone__phone=username)
        
            
        if user.check_password(password):

            return user
        
        else:

            # if not User.objects.filter(email=username).exists():

            #     messages.warning(request,'Email not found')
            return None

        # try:
        #     user=User.objects.filter(Q(username=username) | Q(email=username)).first()

        # except User.DoesNotExist:
           
        #     return  None
        # if user and check_password(user, user.password):
        #     return user
       
        # else:
        #     return None