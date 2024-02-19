from django.shortcuts import render
from product_categories.models.product_brand import Product_Brand
from products.models.products_model import Products,Customer_Review
from django.core.paginator import Paginator


def show_product_brand_wise(request,pk):
    
    brand_wise = Products.objects.filter(product_brand=pk)

    for product in brand_wise:
        reviews_count = Customer_Review.objects.filter(products=product.id).count()
        # wish_list= Wish_List.objects.filter(user=request.user, products=product.id, is_added=True)
        # print("Wish list++++++++",wish_list)

    # Create a Paginator instance
    paginator = Paginator(brand_wise,9)
    print("Pagination for cat ----", paginator)

    # Get the current page number from the request's GET parameters

    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context ={
      
        'fatch_all_products' : paged_product,
        'brand_wise' :brand_wise,
        'reviews_count' :reviews_count,
        
    }

    return render(request,'brands/brands.html', context=context)