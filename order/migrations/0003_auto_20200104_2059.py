# Generated by Django 2.2.6 on 2020-01-04 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_shippingorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingorder',
            name='comment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='shippingorder',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
