from django.db import models
from product_categories.models.product_category import Product_Categories
from product_categories.models.product_brand import Product_Brand

# Create your models here.


    


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='products')
    product_price = models.FloatField()
    product_old_price = models.FloatField()
    product_discription = models.TextField()
    
    product_brand = models.ForeignKey(Product_Brand, on_delete=models.CASCADE, related_name='product_prand')
    product_category = models.ForeignKey(Product_Categories, on_delete=models.CASCADE, related_name='category')
    

    def __str__(self) -> str:
        return self.product_name
    




