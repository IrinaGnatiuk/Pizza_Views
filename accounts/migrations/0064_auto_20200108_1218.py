# Generated by Django 2.2.6 on 2020-01-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20200104_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='ac59302ab10d42aa8bd64d1663b7dcc55e26f1e69ffa47459dec3e2da97a04f0', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='6cbc7cb9776e475f902526fb8efb6ef590e55c7169dc445a9e2191b2c6c8bac8', max_length=300, null=True),
        ),
    ]
