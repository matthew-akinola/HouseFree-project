# Generated by Django 3.2.10 on 2022-09-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_auto_20220902_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='short_id',
            field=models.CharField(default='5TUQMU18C', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default='RJAIC73TS', max_length=255, unique=True),
        ),
    ]
