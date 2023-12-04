from product_categories.models.product_category import Product_Categories


def categories(request):

    category_name = Product_Categories.objects.all()

    print("Category name +++++++++++++++", category_name)
    
    return {'category_name' : category_name}

