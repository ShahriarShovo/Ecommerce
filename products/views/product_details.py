from django.shortcuts import render, get_object_or_404
from products.models.products_model import Products,Customer_Review
#from products.models.customer_review import Customer_Review
from products.models.old_product_variation import Variation
from django.db.models import Avg
from products.models.product_gallary import Product_Gallery
from products.models.product_variation.size_variant import Product_Size_variant
from orders.models.product_ordered import Products_Ordered

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)

    #print(product_details.pk)

    reviews_count = Customer_Review.objects.filter(products=product_details).count()
    request_user = request.user

    product_gallery = Product_Gallery.objects.filter(product=product_details)

    total_product_order_count= Products_Ordered.objects.filter(product_name__pk=product_details.pk).count()

    # print ("Total order this product ___________", total_product_order_count)
    
    context={
        'product_details' : product_details,
      
        'reviews_count' :reviews_count,
        "request_user": request_user,
        'product_gallery':product_gallery,
        'total_product_order_count' :total_product_order_count,
    }

    if request.GET.get('size'):
        size = request.GET.get('size')
        size_object = get_object_or_404(Product_Size_variant, size_name=size)
        size_pk = size_object.pk
        #print("Size Pk_____________-", size_pk)
        request.session['size']=size
        request.session['size_pk']=size_pk
        depend_on_size_price = product_details.get_product_price_by_size(size)

        context['selected_size']=size
        
        context['depend_on_size_price']=depend_on_size_price

    # if request.GET.get('color'):

    #     color = request.GET.get('color')
    #     print("Get color !!!!!!!!!!!!!!!!!!!!!",color)
    #     selected_color=request.session['selected']=color
    #     print('add color in session',selected_color )
    
    if request.user.is_authenticated:
        get_review_product_ordered= Products_Ordered.objects.filter(ordered__user=request.user, product_name__pk=product_details.pk, ordered__status='Completed'  )
        #print(get_review_product_ordered)
        context['get_review_product_ordered']=get_review_product_ordered

    # if request.method == 'POST':
    get_code = request.POST.get('get_code')

    # print("coupon code in single product +++++++++++++++++", get_code)
        

       

    return render(request, 'product_page/product_details.html', context=context)