from django.db import models
from product_categories.models.product_category import Product_Categories
from product_categories.models.product_brand import Product_Brand
from products.models.product_variation.size_variant import Product_Size_variant
from products.models.product_variation.color_variant import Product_Color_Variant
from products.models.delivery_country import Product_Delivery_Country


# Create your models here.


class Products(models.Model):
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
    

    def __str__(self) -> str:
        return self.product_name
    

    def get_product_price_by_size(self,size):

        return self.product_price + Product_Size_variant.objects.get(size_name=size).price
    


    

    




