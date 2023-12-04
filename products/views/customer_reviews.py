from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from products.models.customer_review import Customer_Review
from products.models.products_model import Products


def customer_reviews(request,pk):


    print("Primary key --+++++++++++++++++++++", pk)
    product = get_object_or_404(Products, pk=pk)
    comment = Customer_Review.objects.filter(products=product)
    
   
    if request.method=="POST":

        comment = request.POST.get('comment')
        print("comments ________________", comment)
    
        if comment == "":
            return HttpResponse("add text in text area")
        
        else:
            Customer_Review.objects.create(user=request.user, products=product,comment_area=comment)
            return redirect('product_detail',pk)
        

    else:
        return HttpResponse("Error")
        

    
    


    