from django.urls import path
from product_categories.views.show_product_cat_wish import show_product_cat_wise


urlpatterns = [
    path('show_product_cat_wise/<int:pk>/', show_product_cat_wise , name='show_product_cat_wise')
]
