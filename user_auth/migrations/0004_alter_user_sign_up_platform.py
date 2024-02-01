# Generated by Django 4.2.4 on 2024-02-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_remove_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sign_up_platform',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Login from Google'), (2, 'Login from Github'), (3, 'Login from Facebook'), (4, 'Login')], null=True),
        ),
    ]
