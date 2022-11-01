# Generated by Django 4.1.2 on 2022-11-01 19:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("custom_users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportCard",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "N1",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "N2",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "N3",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "N4",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("is_approved", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "average",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                (
                    "attendance",
                    models.DecimalField(decimal_places=2, default=100.0, max_digits=5),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="report_cards",
                        to="custom_users.student",
                    ),
                ),
            ],
        ),
    ]
