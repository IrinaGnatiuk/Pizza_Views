# Generated by Django 2.2.6 on 2019-11-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191117_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='de1da2f719444dba8e3542b6053c6b2b0759bd80be5742e784c183a078a4cb55', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='f3f64df5f7674c66abf60c43449a56993ddb3869a689499db8b66759449f92d9', max_length=300, null=True),
        ),
    ]