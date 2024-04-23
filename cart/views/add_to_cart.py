from django.shortcuts import render, get_object_or_404 , redirect, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products
from products.models.product_variation.size_variant import Product_Size_variant
from django.http import HttpResponseRedirect
from cart.models.cart_item import Cart_Item




# def add_to_cart(request, pk):
#     product_item = get_object_or_404(Products, pk=pk)
#     user= request.user
#     size_variant = request.GET.get('size')

#     cart , _ = Cart.objects.get_or_create(user=user, is_paid=False)
#     cart_item = Cart_Item.objects.create(cart=cart, product=product_item,)

#     if size_variant:
#         size = request.GET.get('size')
#         s_variant = Product_Size_variant.objects.get(size_name=size)
#         cart_item.product_Size_variant=s_variant
#         cart_item.save()

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.db.models import F

def add_to_cart(request, pk):
    product_item = get_object_or_404(Products, pk=pk)
    user = request.user
    size_variant = request.GET.get('size')

    # Get the user's cart
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    # Check if the product with the same size variant already exists in the cart
    existing_cart_item = cart.cart_item.filter(product=product_item, product_Size_variant__size_name=size_variant).first()

    if existing_cart_item:
        # If the product with the same size variant exists, increase its quantity
        existing_cart_item.quantity = F('quantity') + 1
        existing_cart_item.save()
    else:
        # If the product with the same size variant doesn't exist, create a new cart item
        cart_item = Cart_Item.objects.create(cart=cart, product=product_item, quantity=1)
        
        if size_variant:
            # If a size variant is provided, link it to the cart item
            s_variant = Product_Size_variant.objects.get(size_name=size_variant)
            cart_item.product_Size_variant = s_variant
            cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

