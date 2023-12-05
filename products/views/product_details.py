from django.shortcuts import render
from products.models.products_model import Products
from products.models.customer_review import Customer_Review

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)

    context={
        'product_details' : product_details,
    }

    return render(request, 'product_page/product_details.html', context=context)