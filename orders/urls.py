from django.urls import path, include
from orders.views.initial_order import initial_order
from orders.views.guest_initial_order import guest_initial_order
from orders.views.choose_payment import choose_payment
from orders.views.buy_now import buy_now




urlpatterns = [
    
     path('review_cart/', initial_order, name='initial_order'), 
     path('review_cart/', guest_initial_order, name='guest_initial_order'), 
     path('choose_payment/', choose_payment, name='choose_payment'),

     path('buy_now/<int:pk>/', buy_now, name='buy_now')


     
     

]
