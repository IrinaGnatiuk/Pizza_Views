# Generated by Django 2.2.6 on 2019-11-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20191124_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='d0faca3706ec452ebcac6376109277e22bd211b991cb40659f5d82f334b629f2', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='8bd4317c2ed44dc0a99f6cf5abbd821e8497097c37604419bf60fd6dbeafe9e1', max_length=300, null=True),
        ),
    ]