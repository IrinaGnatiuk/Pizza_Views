# Generated by Django 2.2.6 on 2019-11-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20191130_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='0e01ca5095ee4b21b20ff62898cc9342f703595718844a6b966d525802eee855', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='b82211eff8d6459992aaeae985ef7b2a847fb685819a48bfb70f0f22b373930e', max_length=300, null=True),
        ),
    ]
