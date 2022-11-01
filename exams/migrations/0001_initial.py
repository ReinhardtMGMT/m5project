# Generated by Django 4.1.2 on 2022-11-01 02:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("report_cards", "0001_initial"),
        ("subjects", "0001_initial"),
        ("custom_users", "0001_initial"),
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
                ("name", models.CharField(max_length=66)),
                (
                    "report_card",
                    models.ForeignKey(
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
