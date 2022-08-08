# Generated by Django 3.2.10 on 2022-07-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "Location",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile/"
                    ),
                ),
                (
                    "background_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile/"
                    ),
                ),
            ],
        ),
    ]
