from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from products.models.customer_review import Customer_Review
from products.models.models import Products


def customer_reviews(request,pk):
    print("Primary key --+++++++++++++++++++++", pk)
    product = get_object_or_404(Products, pk=pk)
   
    if request.method=="POST":
        comment = request.POST.get('comment')
        print("comment key --+++++++++++++++++++++", comment)
        if comment:
            Customer_Review.objects.create(
                user=request.user,
                products=product,
                comment_area=comment,
            )
            return redirect('product_detail',pk)
        elif comment == '':
            return HttpResponse("add text in text area")
        else:
            return HttpResponse("erro")
    else:
        return HttpResponse("Error")
        

    
    


    