from product_categories.models.product_brand import Product_Brand


def brands(request):

    brand_name = Product_Brand.objects.all()
    #print("brand name +++++++++++++++", brand_name)
    return {'brand_name': brand_name}