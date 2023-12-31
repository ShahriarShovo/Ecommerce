from django.contrib import admin
from django.urls import path, include
from products.views.products import index
from products.views.product_details import product_detail
from products.views.review.customer_reviews import customer_reviews
from products.views.view_product_price_range import view_product_price_range
# from products.views.review.fatch_user_review import fatch_user_review
from products.views.review.delete_review import delete_review




#app_name='products'

urlpatterns = [
    path('', index, name='index'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('review/<int:pk>/', customer_reviews, name='customer_reviews'),
    path('price_range/', view_product_price_range, name='get_product_price_range'),
    #path('reviews/', fatch_user_review, name='fatch_user_review'),
    path('delete_reviews/<int:pk>/', delete_review, name='delete_review'),


]