from django.urls import path, include
from orders.views.authenticated_initial_order import initial_order
from orders.views.guest_initial_order import guest_initial_order





urlpatterns = [
    
     path('review_cart/', initial_order, name='initial_order'), 
     path('review_cart/', guest_initial_order, name='guest_initial_order'), 
     
     

]
