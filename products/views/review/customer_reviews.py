from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from products.models.customer_review import Customer_Review
from products.models.products_model import Products


def customer_reviews(request,pk):

    if request.method == "POST":
        product = get_object_or_404(Products, pk=pk)
        print("Primary key --+++++++++++++++++++++", pk)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        print("comments ________________", comment)
        print("rating ________________", rating)
        user = request.user
        print("user ________________", user)

        if Customer_Review.objects.filter(user=user, products=product):
            print("dont create a comment ++++++++++++++++++++=")
            return redirect('product_detail',pk)
        else :
            Customer_Review.objects.create(user=user, products=product,comment_area=comment,rating=rating)
            print("working ++++++++++++++++++++=")
            return redirect('product_detail',pk)
            

        




    # print("Primary key --+++++++++++++++++++++", pk)
    # product = get_object_or_404(Products, pk=pk)

    # comment = Customer_Review.objects.filter(products=product)
    
   
    # if request.method=="POST":

    #     comment = request.POST.get('comment')
    #     print("comments ________________", comment)
    
    #     if comment == "":
    #         return HttpResponse("add text in text area")
        
    #     else:
    #         Customer_Review.objects.create(user=request.user, products=product,comment_area=comment)
    #         return redirect('product_detail',pk)
        

    # else:
    #     return HttpResponse("Error")

    
        

    
    


    