# Generated by Django 2.2.6 on 2019-12-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_auto_20191214_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='ef84e099df444aa4b6280cbacf355fe781ba00c9963541d1bd6bbe309a2468a2', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='ce81c8828882412fb1e4d52a8968ca00fb168e099a864334b286bd0211ea31df', max_length=300, null=True),
        ),
    ]
