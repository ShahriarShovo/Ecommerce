from django.shortcuts import render
from products.models.models import Products

# # Create your views here.

def all_products(reques):
    all_product= Products.objects.all()
    return render(reques, 'admin/products/product_list.html', locals())