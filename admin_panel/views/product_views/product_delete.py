from django.shortcuts import render, redirect
from products.models.models import Products

def product_delete(request,pk):
    
    delete_current_product= Products.objects.get(pk=pk).delete()
    return redirect('all_products')