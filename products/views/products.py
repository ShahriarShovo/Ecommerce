from django.shortcuts import render
from products.models.products_model import Products,Customer_Review
from django.core.paginator import Paginator
from cart.models.wish_list import Wish_List
from system_setting.models.banner import Banner
from orders.models.product_ordered import Products_Ordered
from django.db.models import Min,Max


# Create your views here.

def index(request):

    fatch_all_products = Products.objects.all()

    min_price = Products.objects.all().aggregate(Min('product_price'))
    max_price = Products.objects.all().aggregate(Max('product_price'))
    # print(min_price)
    # print(max_price)

    FilterPrice = request.GET.get('FilterPrice')

    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        fatch_all_products = Products.objects.filter(product_price__lte = Int_FilterPrice)

        # print('fatch_all_products++++++++++++',fatch_all_products)
        
    banners = Banner.objects.all()

    
    for product in fatch_all_products:
        reviews_count = Customer_Review.objects.filter(products=product.id).count()
    
        if request.user.is_authenticated :
            wish_list= Wish_List.objects.filter(user=request.user, products=product.id, is_added=True)
            
            # print("Wish list++++++++",wish_list)
        else:
            wish_list = None
        
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
        'min_price':min_price,
        'max_price':max_price,
        'FilterPrice':FilterPrice,
       
    }
    
    return render(request, 'index/index.html', context)

