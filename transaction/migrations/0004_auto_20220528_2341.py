# Generated by Django 3.2.10 on 2022-05-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20220523_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='short_id',
            field=models.CharField(default='B3HLCFO15', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_id',
            field=models.CharField(default='QWDO5CRHK', max_length=255, unique=True),
        ),
    ]