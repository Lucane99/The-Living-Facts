# Generated by Django 5.0.3 on 2025-03-15 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

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
                ("bio", models.TextField(blank=True)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("location", models.CharField(blank=True, max_length=255)),
                ("website", models.URLField(blank=True, max_length=255)),
                ("phone_number", models.CharField(blank=True, max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
