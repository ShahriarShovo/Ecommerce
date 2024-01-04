from django.db import models
from product_categories.models.product_category import Product_Categories
from product_categories.models.product_brand import Product_Brand
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.delivery_country import Product_Delivery_Country
from user_auth.models.user import User
from django.db.models import Avg, Count


# Create your models here.


class Products(models.Model):
    in_stock=1
    out_of_stock=2

    free=1
    not_free=2

    available = ((in_stock,'In Stoke') , (out_of_stock,'Out of Stock'))
    shipping_fee= ((free,'Free') , (not_free,'Not Free'))

    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='products')
    product_price = models.FloatField()
    product_old_price = models.FloatField()
    product_discription = models.TextField()
    model = models.CharField(max_length=50, blank=True, null=True)
    product_brand = models.ForeignKey(Product_Brand, on_delete=models.CASCADE, related_name='product_prand')
    product_category = models.ForeignKey(Product_Categories, on_delete=models.CASCADE, related_name='category')
    product_delivery_country = models.ManyToManyField(Product_Delivery_Country,  null=True, blank=True)
    product_size = models.ManyToManyField(Product_Size_variant,  null=True, blank=True)
    product_color = models.ManyToManyField(Product_Color_Variant,  null=True, blank=True)
    available_choose = models.PositiveSmallIntegerField(choices=available,blank=True, null=True)
    shipping_fee = models.PositiveSmallIntegerField(choices=shipping_fee,blank=True, null=True)
    

    def __str__(self) -> str:
        return self.product_name
    

    def get_product_price_by_size(self,size):

        return self.product_price + Product_Size_variant.objects.get(size_name=size).price
    
    def averageRating(self):
        reviews = Customer_Review.objects.filter(products=self,status=True).aggregate(average=Avg('rating'))
        avg=0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def count_reviews(self):
        reviews = Customer_Review.objects.filter(products=self,status=True).aggregate(count=Count('rating'))
        count=0
        if reviews['count'] is not None:
            avg = int(reviews['count'])
        return avg
    

    # def get_total_for_single_product(self):
    #     #total = self.product_price * self.quantity
    #     total = self.product_price
    #     float_total = format( total, '0.2f')
    #     print(' cart each_total -----------------------', float_total)
    #     return float_total
    


class Customer_Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_review')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products_review')
    comment_title = models.CharField(max_length=200,null=True,blank=True)
    comment_area = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=200,null=True,blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.user.email
    


    

    




