# Generated by Django 2.2.6 on 2019-11-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191117_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='d818307e068a441aabee57ae4560b3e5bc7992a68742463b9c72725bdc44b725', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='ce338b30e4e642be933b5f6d6568074ddb7cf5c391014183825ef9177d29e69d', max_length=300, null=True),
        ),
    ]