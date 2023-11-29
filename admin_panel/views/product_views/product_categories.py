from django.shortcuts import render, redirect, HttpResponse
from product_categories.models.models import Product_Categories


def fatch_categories(request):
    fatch_cat = Product_Categories.objects.all()
    return render(request, 'admin/products/product_categories.html', locals())


def add_category(request):
    if request.method=="POST":
        get_cat = request.POST.get('category_name')
        if get_cat == '':
            return HttpResponse("Please add some word")
        else:
            if Product_Categories.objects.filter(category_name=get_cat):
                return HttpResponse("Already Exist")
            else:
                create_new_cat = Product_Categories.objects.create(category_name=get_cat)
                return redirect('fatch_categories')
    else:
        return HttpResponse("Failed to Add Category")
   

def update_categories(request,pk):
    get_cat_id = Product_Categories.objects.get(pk=pk)
    if request.method=="POST":
        get_cat_data = request.POST.get('update_category')
        if get_cat_data == '':
            return HttpResponse('Input field is empty ')
        else:
            get_cat_id.category_name = get_cat_data
            get_cat_id.save()
            return redirect('fatch_categories')
    return render(request, 'admin/products/update_categories.html', locals())


def delete_category(request,pk):
    delete_category= Product_Categories.objects.get(pk=pk).delete()
    return redirect('fatch_categories')
