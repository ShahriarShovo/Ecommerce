from django.shortcuts import render
from products.models.models import Products
from products.models.customer_review import Customer_Review

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)

    # if request.method == "POST":
    #     comment = request.POST.get('comment')
    #     print("Comment--------------------------", comment)

    context={
        'product_details' : product_details,
    }

    return render(request, 'product_page/product_details.html', context=context)