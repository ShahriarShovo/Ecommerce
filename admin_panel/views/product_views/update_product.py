from django.shortcuts import render, redirect
from products.models.products_model import Products
from product_categories.models.product_category import Product_Categories

def update_product(request,pk):

    current_product_update = Products.objects.get(pk=pk)
    
    if request.method == "POST":
        get_cat_id= request.POST.get('category')
        print("Cat---------------",get_cat_id)
        image = request.FILES.get('image')
        get_p_name = request.POST.get('p_name')
        p_price = request.POST.get('p_price')
        p_old_price = request.POST.get('p_old_price')
        p_brand = request.POST.get('p_brand')
        p_discription = request.POST.get('p_discription')
        get_current_p_cat_id = Product_Categories.objects.get(pk=get_cat_id)

        current_product_update.product_category=get_current_p_cat_id
        current_product_update.product_name=get_p_name
        current_product_update.product_image=image
        
        current_product_update.product_price=p_price
        current_product_update.product_old_price=p_old_price
        current_product_update.product_brand=p_brand
        current_product_update.product_discription=p_discription
        current_product_update.save()

        return redirect('all_products')

    return render(request, 'admin/products/update_product.html', locals())