# Generated by Django 2.2.6 on 2020-01-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_dish_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
