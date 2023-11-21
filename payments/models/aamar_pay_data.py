from django.db import models


class aamar_pay_data(models.Model):

    email= models.EmailField()
    datas = models.JSONField()

    def __str__(self) -> str:
        return self.email