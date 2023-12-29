from django.db import models


class Product_Delivery_Country(models.Model):
    
    country_name = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return self.country_name