from django.shortcuts import render
from products.models.products_model import Products
from products.models.customer_review import Customer_Review
from products.models.old_product_variation import Variation

# Create your views here.



def product_detail(request, pk):

    product_details = Products.objects.get(pk=pk)
    

    context={
        'product_details' : product_details,
    }

    if request.GET.get('size'):
        size = request.GET.get('size')
        

        depend_on_size_price = product_details.get_product_price_by_size(size)

        context['selected_size']=size
        
        context['depend_on_size_price']=depend_on_size_price

    # if request.GET.get('color'):

    #     color = request.GET.get('color')
    #     print("Get color !!!!!!!!!!!!!!!!!!!!!",color)
    #     selected_color=request.session['selected']=color
    #     print('add color in session',selected_color )

       

    return render(request, 'product_page/product_details.html', context=context)