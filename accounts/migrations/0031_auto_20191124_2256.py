# Generated by Django 2.2.6 on 2019-11-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20191124_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='aa17ff312f104422bd061f862bc8bdfbb42591d548a94b88acf4bbecbb96598d', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='8197adf48bb345348dc317ae6f1c63d17863a957ce994ccfb0f15c93f75f2a03', max_length=300, null=True),
        ),
    ]
