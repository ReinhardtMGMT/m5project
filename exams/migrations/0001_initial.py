# Generated by Django 4.1.3 on 2022-11-10 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("custom_users", "0002_initial"),
        ("report_cards", "0001_initial"),
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exams",
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
                    "score",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("description", models.TextField()),
                ("date", models.DateField()),
                (
                    "quarter",
                    models.TextField(
                        choices=[("q1", "Q1"), ("q2", "Q2"), ("q3", "Q3"), ("q4", "Q4")]
                    ),
                ),
                (
                    "report_card",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exams",
                        to="report_cards.reportcard",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exams",
                        to="custom_users.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exams",
                        to="subjects.subject",
                    ),
                ),
            ],
        ),
    ]
