# Generated by Django 2.2.6 on 2019-11-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191112_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='950a93a1106f45488914d1e221a499896ffd6d908c974e129ee023dc6797ba04', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='49a6cb75e23846eda52ba746c2cb9deae39b1f3d1685448fb736f3bacc08f195', max_length=300, null=True),
        ),
    ]
