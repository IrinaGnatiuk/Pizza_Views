# Generated by Django 2.2.6 on 2019-11-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20191125_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='97474526a6b24825988581ebd8c352f2b24c13294a7a45ae99c89812345f0aec', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='0e44e239b911451d950fb54549fefa155ec0b518e8b64da3ade22f6a277d721d', max_length=300, null=True),
        ),
    ]
