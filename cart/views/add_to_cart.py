from django.shortcuts import render, get_object_or_404 , redirect, HttpResponse
from cart.models.cart import Cart
from orders.models.orders import Order
from products.models.products_model import Products
from products.models.product_variation.size_variant import Product_Size_variant
from django.http import HttpResponseRedirect
from cart.models.cart_item import Cart_Item




def add_to_cart(request, pk):
    product_item = get_object_or_404(Products, pk=pk)
    user= request.user
    size_variant = request.GET.get('size')

    cart , _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = Cart_Item.objects.create(cart=cart, product=product_item,)

    if size_variant:
        size = request.GET.get('size')
        s_variant = Product_Size_variant.objects.get(size_name=size)
        cart_item.product_Size_variant=s_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
