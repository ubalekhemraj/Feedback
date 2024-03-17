# Generated by Django 5.0.3 on 2024-03-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("food_rating", models.CharField(max_length=20)),
                ("recommendation", models.IntegerField()),
                ("name", models.CharField(blank=True, max_length=100)),
                ("mobile_number", models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]