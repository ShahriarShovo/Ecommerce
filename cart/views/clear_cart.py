from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from cart.models.cart_item import Cart_Item

def clear_cart(request):
    get_cart_items = Cart_Item.objects.filter(cart__user=request.user)
    get_cart_items.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))