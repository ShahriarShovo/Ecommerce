from django.shortcuts import render, redirect, HttpResponse
from product_categories.models.product_category import Product_Categories
from products.models.products_model import Products

def show_product_cat_wise(request,pk):

    show_prodct_cat_wise= Products.objects.filter(product_category=pk)

    print("Product Category ++++++++++++++++++++", show_prodct_cat_wise)

    return render(request,'category/show_cat_wise_product.htm', locals())