# Generated by Django 2.2.6 on 2019-11-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20191117_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='b9aef419a68047658d04ab7d9275225df125aeb7d34d45fd9d43450d941f6964', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='f6892870432c432c8814fbf97308a81076ce1092e4bf4e91ad4382411c7927f5', max_length=300, null=True),
        ),
    ]
