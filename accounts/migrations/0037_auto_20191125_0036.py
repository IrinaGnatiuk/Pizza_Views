# Generated by Django 2.2.6 on 2019-11-24 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20191124_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='8a6969c697944641a6f9d18feb4327771f7c41dbc47a4361b095a36f9c6e8b69', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='638e8f35fe8443c6a2d72d5288c4e9f20d02fd0623c34b0aafddc9773808f971', max_length=300, null=True),
        ),
    ]