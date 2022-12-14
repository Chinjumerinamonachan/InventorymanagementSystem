# Generated by Django 4.1 on 2022-09-16 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("lattitude", models.FloatField(max_length=150)),
                ("longitude", models.FloatField(max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("building_name", models.CharField(max_length=120)),
                ("street", models.CharField(max_length=120)),
                ("city", models.CharField(max_length=100)),
                ("district", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=10)),
                ("post_office", models.CharField(max_length=10)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="master.location",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
