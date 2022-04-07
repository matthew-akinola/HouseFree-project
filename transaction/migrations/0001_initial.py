# Generated by Django 3.2.10 on 2022-04-07 10:53

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='phone number')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=40)),
                ('agent_account_number', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, null=True)),
                ('room_id', models.CharField(default='2U6QHMIP2', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('account_number', models.CharField(max_length=20)),
                ('account_bank', models.CharField(max_length=4)),
                ('amount', models.CharField(max_length=20)),
                ('narration', models.CharField(max_length=200)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('NGN', 'NGN')], max_length=3)),
                ('reference', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('debit_currency', models.CharField(choices=[('USD', 'USD'), ('NGN', 'NGN')], max_length=3)),
                ('account_id', models.CharField(max_length=60)),
                ('withdrawal_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sender', models.CharField(max_length=30, null=True)),
                ('recipient', models.CharField(blank=True, max_length=60, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('date_sent', models.CharField(blank=True, max_length=60, null=True)),
                ('amount', models.CharField(max_length=40)),
                ('agent_account_number', models.CharField(max_length=150)),
                ('account_number', models.CharField(max_length=20, null=True)),
                ('history_time', models.DateTimeField(auto_now_add=True)),
                ('account_bank', models.CharField(max_length=4, null=True)),
                ('narration', models.CharField(max_length=200, null=True)),
                ('reference', models.CharField(blank=True, max_length=150, null=True)),
                ('debit_currency', models.CharField(max_length=3, null=True)),
                ('account_id', models.CharField(blank=True, max_length=60, null=True)),
                ('transaction_status', models.CharField(max_length=12, null=True)),
                ('withdrawal_date', models.CharField(blank=True, max_length=60, null=True)),
                ('short_id', models.CharField(default='BNOM4E3FZ', max_length=255, unique=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='transaction.rooms')),
            ],
            options={
                'ordering': ['-history_time'],
            },
        ),
    ]
