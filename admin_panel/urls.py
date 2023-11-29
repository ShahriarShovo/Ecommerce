from django.urls import path
from .views.index.index_view import admin_home

from .views.product_views.all_product import all_products
from .views.product_views.add_product import add_product
from .views.product_views.update_product import update_product
from .views.product_views.product_delete import product_delete
from .views.product_views.product_categories import (fatch_categories,
                                                     add_category,
                                                     update_categories, 
                                                     delete_category)

from .views.user.fatch_user import fatch_user


urlpatterns = [
    path('', admin_home, name='admin_home'),

    path('products/', all_products, name='all_products'),
    path('product_add/', add_product, name='add_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('update_delete/<int:pk>/', product_delete, name='product_delete'),

    path('categories/', fatch_categories, name='fatch_categories'),
    path('add_category/', add_category, name ='add_category'),
    path('update_categories/<int:pk>/', update_categories, name='update_categories'),
    path('delete_category/<int:pk>/', delete_category, name='delete_category'),

    path('user_list/', fatch_user, name='fatch_user'),



    
]
