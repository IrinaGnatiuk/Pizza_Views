# Generated by Django 2.2.6 on 2019-11-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20191121_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='2664eca1bc724d2193e4059b704ebcd4b1253e40fd8f44b9ab59b427acb9c25c', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='5d940aca3fd24042be749b0000f37bd7bdc9d8de8997486a8473a748f6518b26', max_length=300, null=True),
        ),
    ]