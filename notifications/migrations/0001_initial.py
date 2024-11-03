# Generated by Django 5.0.4 on 2024-11-03 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                ("message", models.CharField(max_length=255)),
                ("scheduled_time", models.TimeField()),
                ("sent", models.BooleanField(default=False)),
                ("seen", models.BooleanField(default=False)),
                (
                    "habit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to="habits.habit",
                    ),
                ),
            ],
        ),
    ]
