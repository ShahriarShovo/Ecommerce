from django.shortcuts import render
from product_categories.models.product_brand import Product_Brand
from products.models.products_model import Products


def show_product_brand_wise(request,pk):
    
    brand_wise = Products.objects.filter(product_brand=pk)
    return render(request,'brands/brands.html', locals())