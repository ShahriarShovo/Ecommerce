from django.urls import path, include
from orders.views.initial_order import initial_order





urlpatterns = [
    
     path('review_cart/', initial_order, name='initial_order'), 
     
     

]
