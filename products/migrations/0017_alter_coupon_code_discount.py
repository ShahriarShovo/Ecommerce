# Generated by Django 4.2.4 on 2024-01-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon_code',
            name='discount',
            field=models.IntegerField(default=100),
        ),
    ]