from django.urls import path
from product_categories.views.show_product_cat_wise import show_product_cat_wise
from product_categories.views.show_product_brand_wise import show_product_brand_wise


urlpatterns = [
    path('show_product_cat_wise/<int:pk>/', show_product_cat_wise , name='show_product_cat_wise'),
    path('show_product_brand_wise/<int:pk>/', show_product_brand_wise , name='show_product_brand_wise')
]
