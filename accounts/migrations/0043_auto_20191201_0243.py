# Generated by Django 2.2.6 on 2019-12-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20191130_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='136fa2a4fec34ae6a5fc4a4241c4a53e5ede2a92ba6e411db302506a4aed4429', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='3bc0aad7faec45e9b307376e53a4a25b5b6253d7070344b593106683032524ec', max_length=300, null=True),
        ),
    ]
