from django.contrib import admin
from user_auth.models.user import User
from user_auth.models.user_profile import Profile
from user_auth.models.guest_user import Guest_User

from django.contrib.auth.admin import UserAdmin


# Register your models here.

class Custom_User_Admin(UserAdmin):
    filter_horizontal                     =                   ()
    list_filter                           =                   ()
    fieldsets                             =                   ()
    list_display                          =                   ('first_name','last_name',
                                                              'username','email','is_active','is_admin','sign_up_platform','created_date','modify_date',)

     
admin.site.register(User,Custom_User_Admin)
admin.site.register(Profile)
admin.site.register(Guest_User)





