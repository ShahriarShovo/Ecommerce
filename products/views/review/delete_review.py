from django.shortcuts import redirect,get_object_or_404
#from products.models.customer_review import Customer_Review
from products.models.products_model import Products,Customer_Review



def delete_review(request,pk):

    user = request.user
    product = get_object_or_404(Products, pk=pk)

    user_review= Customer_Review.objects.filter(user=user, products=product)
    
    if user_review:
            delete= user_review.delete()
            print("working ++++++++++++++++++++=")
            return redirect('product_detail',pk)
