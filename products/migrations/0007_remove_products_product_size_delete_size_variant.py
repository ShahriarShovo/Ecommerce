# Generated by Django 4.2.4 on 2023-12-26 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_size_variant_products_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_size',
        ),
        migrations.DeleteModel(
            name='Size_variant',
        ),
    ]