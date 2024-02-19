from django.shortcuts import render, redirect, HttpResponse
from product_categories.models.product_category import Product_Categories
from products.models.products_model import Products,Customer_Review
from django.core.paginator import Paginator

def show_product_cat_wise(request,pk):

    show_prodct_cat_wise= Products.objects.filter(product_category=pk)

    for product in show_prodct_cat_wise:
        reviews_count = Customer_Review.objects.filter(products=product.id).count()
        # wish_list= Wish_List.objects.filter(user=request.user, products=product.id, is_added=True)
        # print("Wish list++++++++",wish_list)

    # Create a Paginator instance
    paginator = Paginator(show_prodct_cat_wise,9)
    print("Pagination for cat ----", paginator)

    # Get the current page number from the request's GET parameters

    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context ={
      
        'fatch_all_products' : paged_product,
        'show_prodct_cat_wise' :show_prodct_cat_wise,
        'reviews_count' :reviews_count,
        
    }

    # print("Pagination for cat ----", paged_product)

    return render(request,'category/show_cat_wise_product.htm', context=context)