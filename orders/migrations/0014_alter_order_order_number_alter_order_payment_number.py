# Generated by Django 4.2.4 on 2024-01-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
