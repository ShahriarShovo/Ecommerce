from django.db import models

class Product_Brand(models.Model):
    
    brand_name = models.CharField(max_length=30)
    brand_created = models.DateTimeField(auto_now=True)
    brand_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.brand_name