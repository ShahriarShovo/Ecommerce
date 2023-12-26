from django.db import models
from products.models.products_model import Products

class VariationManager(models.Manager):

    def size(self):
        return super(VariationManager,self).filter(Variation='size')
    

    def color(self):
        return super(VariationManager,self).filter(Variation='color')


PRODUCT_VARIATION=(
    ('size','size'),
    ('color','color'),
)

class Variation(models.Model):
    Variation = models.CharField(max_length=100, choices=PRODUCT_VARIATION)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price= models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects= VariationManager()

    def __str__(self):
        return self.name
    

    # def get_variation_price(self,size):
    #     return self.product.product_price + Variation.objects.get(Variation=size)
    


    