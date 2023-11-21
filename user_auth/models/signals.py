from django.dispatch import receiver
from django.db.models.signals import post_save
from user_auth.models.user import User
from user_auth.models.user_profile import Profile
from orders.models.billing_address import BillingAddress


@receiver(post_save,sender=User)
def post_save_create_profile_reciver(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            profile=Profile.objects.get(user=instance)
            profile.save()
        except:
            Profile.objects.create(user=instance)

# @receiver(post_save,sender=User)
# def post_save_create_user_billing_address(sender,instance,created, **kwargs):
#     if created:
#         BillingAddress.objects.create(user=instance)
#     else:
#         try:
#             # address=BillingAddress.objects.get(user=instance)
#             # address.save()
#             pass
#         except:
#             BillingAddress.objects.create(user=instance)



