# Generated by Django 2.2.6 on 2019-11-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20191117_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='679974b11dd841ba87c7b6171017e6247682f6c462dd4f9eb5719ce632174f52', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='f819d3bbccc14bf7a99a279fe50da1ee3d1ad12a0f0942e6a3f161e32abf6dbc', max_length=300, null=True),
        ),
    ]
