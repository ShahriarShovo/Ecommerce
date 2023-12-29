from django.shortcuts import render
from products.models.products_model import Products
from products.models.customer_review import Customer_Review
from products.models.old_product_variation import Variation

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)
    variation = Variation.objects.get(pk=pk)

    context={
        'product_details' : product_details,
    }

    if request.GET.get('size'):
        size = request.GET.get('size')
        #print("size ++++++++++++++++++++", size)
        size_price = variation.get_variation_price(size)
        #print("size_price ++++++++++++++++++++", size_price)

    return render(request, 'oldproduct_page/product_details.html', context=context)