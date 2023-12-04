from django.shortcuts import render, redirect, HttpResponse


def view_product_price_range(request):
    
    if request.method=="POST":
        min = request.POST.get('min')
        max = request.POST.get('max')

        print("min+++++++++++++++++++", min)
        print("max+++++++++++++++++++", max)