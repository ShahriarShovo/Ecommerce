# Generated by Django 4.2.4 on 2024-02-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_remove_order_product_products_ordered_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products_ordered',
            name='ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.products_ordered'),
        ),
        migrations.AddField(
            model_name='products_ordered',
            name='payment_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]