# Generated by Django 3.2.10 on 2022-04-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_auto_20220423_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='short_id',
            field=models.CharField(default='1SSOUCWUT', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_id',
            field=models.CharField(default='FIZSAFW9K', max_length=255, unique=True),
        ),
    ]