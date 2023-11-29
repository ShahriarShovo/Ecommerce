
from django.db import models

class Guest_User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.email