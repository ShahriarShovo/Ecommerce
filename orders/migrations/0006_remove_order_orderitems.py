# Generated by Django 4.2.4 on 2023-11-25 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderItems',
        ),
    ]
