# Generated by Django 4.2.4 on 2024-01-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_order_number_alter_order_payment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]