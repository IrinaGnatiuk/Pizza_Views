# Generated by Django 2.2.6 on 2019-11-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_auto_20191130_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='00f8e6ee93044904b93ced834b3887ec2426c841e2964d509b49077f6fbdbab7', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='8035f703426541c195a0a6bb9955b272ea8028e055034dfe98355f970d64e3ea', max_length=300, null=True),
        ),
    ]
