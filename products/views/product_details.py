from django.shortcuts import render
from products.models.products_model import Products
from products.models.customer_review import Customer_Review
from products.models.product_variation import Variation

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)

    context={
        'product_details' : product_details,
    }

    if request.GET.get('size'):
        size = request.GET.get('size')
        print("size ++++++++++++++++++++", size)

    return render(request, 'product_page/product_details.html', context=context)