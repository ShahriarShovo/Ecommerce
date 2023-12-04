from django.shortcuts import render
from products.models.products_model import Products
from product_categories.models.product_category import Product_Categories


def add_product(request):
    

    if request.method == "POST":
        get_cat_id= request.POST.get('category')
        print("Cat---------------",get_cat_id)
        image = request.FILES.get('image')
        get_p_name = request.POST.get('p_name')
        p_price = request.POST.get('p_price')
        p_old_price = request.POST.get('p_old_price')
        p_brand = request.POST.get('p_brand')
        p_discription = request.POST.get('p_discription')

        category_id = Product_Categories.objects.get(pk=get_cat_id)
       
        create_product=Products.objects.create(product_name=get_p_name,product_image=image,
                                               product_price=p_price,product_old_price=p_old_price,
                                               product_brand=p_brand,
                                               product_discription=p_discription,
                                               product_category=category_id)
        #create_product.save()


    return render(request, 'admin/products/add_products.html')