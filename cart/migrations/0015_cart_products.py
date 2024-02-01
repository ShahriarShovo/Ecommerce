# Generated by Django 4.2.4 on 2024-01-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_gallery'),
        ('cart', '0014_cart_grand_total_cart_quantity_cart_tax_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='cart.Cart_Item', to='products.products'),
        ),
    ]