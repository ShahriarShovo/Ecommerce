from django.contrib import admin
from django.urls import path, include
from .views.authentication.user_registration import user_register, activate, check_email
from .views.authentication.user_login import user_login, myaccount
from .views.dashboard.thank_you import thank_you
from .views.password.forget_password import forget_password
from .views.dashboard.user_dashboard import user_dashboard
from .views.authentication.user_logout import user_logout
from .views.social_login.google_login import google_login
from .views.social_login.google_login import google_callback
from .views.social_login.git_hub_login import github_callback, github_login
from .views.social_login.facebook_login import facebook_login,facebook_callback #facebook_login_callback
from .views.password.reset_password import reset_password
from .views.password.reset_password_validate import reset_password_validate
#from .views.dashboard.update_address_view import update_address_view
from .views.dashboard.update_address import update_address
#from .views.user_billing_address import user_billing_address
from user_auth.views.password.change_password import change_password

#app_name='user_auth'
from user_auth.views.dashboard.dashboard_options.total_orders import total_orders
from user_auth.views.dashboard.dashboard_options.order_details_status import order_details_status
from user_auth.views.dashboard.dashboard_options.order_completed import order_completed
from user_auth.views.dashboard.dashboard_options.cash_on_deliverys import cash_on_deliverys
from user_auth.views.dashboard.dashboard_options.paid_delivery import paid_delivery
from user_auth.views.dashboard.deactivate_account import deactivate_account

from user_auth.views.dashboard.dashboard_options.notification import notification


urlpatterns = [
   
    path('login/', user_login, name='user_login'),
    path('user_registration/', user_register, name='user_registration'),
    
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('thank_you/', thank_you, name='thank_you'),
    path('check_email', check_email, name='check_email'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('logout/', user_logout, name='user_logout'),
    path('myaccount/', myaccount, name='myaccount'),
    #path('update_address_view/<int:pk>/', update_address_view, name='update_address_view'),
    path('create_address_view/', update_address, name='update_address'),
    #path('update_user_info', settings, name='update_user_info'),
    #path('update_user_billing_address', user_billing_address, name='update_user_billing_address'),


    #google auth
    path('auth/google_login/', google_login, name='google_login'),
    path('auth/google_callback/', google_callback, name='google_callback'),

    #git hub
    path('auth/github/', github_login, name='github_login'),
    path('auth/github_callback/', github_callback, name='github_callback'),

    #facebook 

    path('facebook-login/', facebook_login, name='facebook_login'),
    path('facebook-callback/', facebook_callback, name='facebook_callback'),
    # Reset password
    path('forget_password/', forget_password, name='forget_password'),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    #path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('reset_password/', reset_password, name='reset_password'),

    path('change-password/', change_password , name='change_password'),


#orders user
    path('total_orders/', total_orders , name='total_orders'),
    path('order_details_status/', order_details_status , name='order_details_status'),
    path('order_completed/', order_completed , name='order_completed'),
    path('cash_on_delivery/', cash_on_deliverys , name='cash_on_deliverys'),
    path('paid_delivery/', paid_delivery , name='paid_delivery'),

    path('deactivate_accound/', deactivate_account , name='deactivate_account'),

    path('notifications/', notification, name='notification'),

    
]
