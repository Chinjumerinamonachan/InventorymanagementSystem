# Generated by Django 4.1.1 on 2022-09-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
