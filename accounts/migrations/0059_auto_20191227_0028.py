# Generated by Django 2.2.6 on 2019-12-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0058_merge_20191227_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='f1932036c197471db0ea96b1869199651ca6dc72b5d44e639a94f77018816b1c', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='bcef17fafd624d6b962a13c6c94201e023641974e7d74987b585cc5ee21fb949', max_length=300, null=True),
        ),
    ]