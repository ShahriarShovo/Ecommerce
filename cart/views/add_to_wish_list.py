from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect,get_object_or_404
from products.models.products_model import Products
from cart.models.wish_list import Wish_List


def add_to_wish_list(request, pk):

    item = Products.objects.get(pk=pk)
    if Wish_List.objects.filter(user=request.user, products=pk, is_added=True).exists():
        return HttpResponse('added')
    else:
        add_wishlist_item = Wish_List.objects.create(products=item, user= request.user, is_added = False)
        add_wishlist_item.is_added=True
        add_wishlist_item.save()
        return redirect('index')


    # user=request.user
    # item = get_object_or_404(Products, pk=pk)
    # wish_listed = Wish_List.objects.filter(user=user, products=item.pk,is_added=True)
    # print(" Already added wish list", wish_listed)

    # if wish_listed.exists():

    #     print(" Already added wish list", wish_listed)
    #     return redirect('index')

    # else:
    #     # add_wishlist_item = Wish_List.objects.create(products=item, user= request.user, is_added = False)
    #     # add_wishlist_item.is_added=True
    #     # add_wishlist_item.save()
    #     # return redirect('index')
    #     return HttpResponse("not added")