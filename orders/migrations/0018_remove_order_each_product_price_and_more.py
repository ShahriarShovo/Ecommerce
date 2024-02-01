# Generated by Django 4.2.4 on 2024-02-01 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_gallery'),
        ('orders', '0017_remove_order_product_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='each_product_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='Products_Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('each_product_price', models.FloatField(blank=True, null=True)),
                ('product_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.products')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.products_ordered'),
        ),
    ]