from django.shortcuts import render
from products.models.products_model import Products
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):

    fatch_all_products = Products.objects.all()

    # items_per_page = 2

    # Create a Paginator instance
    paginator = Paginator(fatch_all_products,6)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    # try:
    #     # Get the Page object for the given page number
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver the first page
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g., 9999), deliver the last page
    #     page_obj = paginator.page(paginator.num_pages)

    context ={
        #'fatch_all_products' : fatch_all_products,
        #'page_obj':page_obj
        'fatch_all_products' : paged_product
    }
    
    return render(request, 'index/index.html', context=context)



def product_detail(request):
    return render(request, 'product_page/product_details.html')
