# Generated by Django 2.2.6 on 2019-12-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20191205_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='99502cba6011465ca9d1bd54127b3b717a22e4c347bd4c84b8cf2ada8b1bc8d5', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='1c430b7f72744a2f843309633c048438322b62d74b194232811c74481dcd9524', max_length=300, null=True),
        ),
    ]
