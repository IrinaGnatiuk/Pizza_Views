# Generated by Django 2.2.6 on 2020-01-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_dish_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]