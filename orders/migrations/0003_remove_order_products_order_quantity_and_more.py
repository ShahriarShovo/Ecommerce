# Generated by Django 4.2.4 on 2023-11-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='select_order_stats',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Cancle'), (2, 'Deliver'), (1, 'Pending')], null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
