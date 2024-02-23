from django.shortcuts import render
from products.models.products_model import Products,Customer_Review
from django.core.paginator import Paginator
from cart.models.wish_list import Wish_List
from system_setting.models.banner import Banner
from orders.models.product_ordered import Products_Ordered


# Create your views here.

def index(request):

    fatch_all_products = Products.objects.all()

    banners = Banner.objects.all()

    for product in fatch_all_products:
        reviews_count = Customer_Review.objects.filter(products=product.id).count()

        if request.user.is_authenticated :
            wish_list= Wish_List.objects.filter(user=request.user, products=product.id, is_added=True)
            
            print("Wish list++++++++",wish_list)
        else:
            wish_list = None
        

        total_product_order_count= Products_Ordered.objects.filter(product_name__pk=product.pk).count()
        print ("Total order this product ___________", total_product_order_count)



        
    
    # Create a Paginator instance
    paginator = Paginator(fatch_all_products,9)

    # Get the current page number from the request's GET parameters

    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    

    

    

    context ={
      
        'fatch_all_products' : paged_product,
        'reviews_count' :reviews_count,
        'wish_list' :wish_list,
        'banners': banners,
        'total_product_order_count' :total_product_order_count
    }
    
    return render(request, 'index/index.html', context=context)

