from django.shortcuts import render, get_object_or_404 , redirect, HttpResponse, HttpResponseRedirect
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products
from products.models.product_variation.size_variant import Product_Size_variant


def add_to_cart(request,pk):

    size_variant = request.GET.get('size')

    product_item = get_object_or_404(Products, pk=pk)

    product_price = product_item.product_price
    
    print("product price ======================",product_price)

    quantity= request.POST.get('quantity')

    print("quantity ======================",quantity)


    if request.user.is_authenticated:

        if size_variant:

            quantity= request.POST.get('quantity')

            print("quantity ======================",quantity)

            size = request.GET.get('size')
            print("add size in cart ======================",size)

            size_variant = Product_Size_variant.objects.get(size_name=size)
            size_variant_price = size_variant.price

            print("size_variant_price ======================",size_variant_price)

            total_product_price = product_price + size_variant_price

            print("total_product_price ======================",total_product_price)

            cart_item = Cart.objects.filter(user=request.user, item=product_item,  purchased = False).first()

            if cart_item:
                cart_item.product_size=size_variant
                cart_item.price=total_product_price
                cart_item.save()
                return redirect("index")

            else:
                
                Cart.objects.create(item=product_item,product_size=size_variant,price=total_product_price, user= request.user, purchased = False)

                return redirect("index")
            
        else:

            cart_item = Cart.objects.filter(user=request.user, item=product_item,  purchased = False).first()

            if cart_item:
                pass

            else:
                
                Cart.objects.create(item=product_item,price=product_price, user= request.user, purchased = False)

                return redirect("index")


    return redirect('index')