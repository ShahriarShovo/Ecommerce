# Generated by Django 4.2.4 on 2024-01-18 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_coupon_code_discount'),
        ('cart', '0011_cart_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon_code'),
        ),
    ]