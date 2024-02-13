# Generated by Django 4.2.4 on 2024-02-13 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_gallery'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0019_wish_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish_list',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wish_list',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_list', to='products.products'),
        ),
    ]
