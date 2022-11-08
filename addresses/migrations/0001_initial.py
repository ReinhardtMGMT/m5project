# Generated by Django 4.1.3 on 2022-11-08 13:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("zipcode", models.CharField(max_length=8)),
                ("district", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=200)),
                ("number", models.CharField(max_length=10)),
            ],
        ),
    ]
