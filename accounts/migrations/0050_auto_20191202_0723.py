# Generated by Django 2.2.6 on 2019-12-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20191202_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='bc08f4986f7e452a89f4fa5465a6432175c93ff3be0f4c8ea1a5f8cc44b45d5c', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='0e9cccff73b24d81abf130cde2e3ff4be089c363ea3d48a4937cb780dc7b8431', max_length=300, null=True),
        ),
    ]