from django.shortcuts import render
from products.models.products_model import Products
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    fatch_all_products = Products.objects.all()
    
    # Create a Paginator instance
    paginator = Paginator(fatch_all_products,6)

    # Get the current page number from the request's GET parameters

    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context ={
      
        'fatch_all_products' : paged_product
    }
    
    return render(request, 'index/index.html', context=context)

