# Generated by Django 4.2.4 on 2023-12-29 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='size',
        ),
    ]
