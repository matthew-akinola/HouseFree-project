# Generated by Django 3.2.10 on 2022-09-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_auto_20220902_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='C7TP2ST7S', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='OPH4PJ860', max_length=255, unique=True),
        ),
    ]
