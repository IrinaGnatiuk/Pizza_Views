# Generated by Django 2.2.6 on 2019-11-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20191117_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='f6728dbfb8b947cead839b2d044270e54a235e0158304b51b31744907ff5d913', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='66ecbc35fc5340a49def4c79659e2072c3fb90fe389d4d039861f37419c2ec3f', max_length=300, null=True),
        ),
    ]
