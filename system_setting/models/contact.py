from django.db import models

class Contact(models.Model):
    city_name=models.CharField(max_length=20, null=True,blank=True)
    city_post_code=models.CharField(max_length=10, null=True,blank=True)
    country_name=models.CharField(max_length=20, null=True,blank=True)
    phone=models.CharField(max_length=20, null=True,blank=True)
    email=models.EmailField(max_length=30, null=True,blank=True)
    telephone=models.CharField(max_length=20, null=True,blank=True)

    company_about=models.TextField( null=True,blank=True)

    def __str__(self) -> str:
        return self.country_name