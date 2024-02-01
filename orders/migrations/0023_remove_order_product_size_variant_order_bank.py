# Generated by Django 4.2.4 on 2024-02-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_products_ordered_product_size_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_Size_variant',
        ),
        migrations.AddField(
            model_name='order',
            name='bank',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]