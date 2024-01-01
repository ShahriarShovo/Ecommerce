# from django.db import models
# from products.models.products_model import Products
# from user_auth.models.user import User




# class Customer_Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_review')
#     products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products_review')
#     comment_title = models.CharField(max_length=200,null=True,blank=True)
#     comment_area = models.TextField(blank=True, null=True)
#     ip = models.CharField(max_length=200,null=True,blank=True)
#     status = models.BooleanField(default=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)


#     rating = models.FloatField(default=0)

#     def __str__(self) -> str:
#         return self.user.email
    


    

