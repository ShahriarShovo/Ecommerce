# Generated by Django 4.2.4 on 2024-01-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_product_size_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_Size_variant',
        ),
    ]
