# Generated by Django 4.1.5 on 2023-01-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cvcreator", "0004_delete_personalinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalInfo",
            fields=[
                ("name", models.CharField(max_length=30)),
                ("idNumber", models.IntegerField(primary_key=True, serialize=False)),
                ("dob", models.DateTimeField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "MALE"), ("female", "FEMALE")], max_length=30
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("telephone", models.CharField(max_length=30)),
                (
                    "maritalStatus",
                    models.CharField(
                        choices=[("married", "MARRIED"), ("single", "SINGLE")],
                        max_length=30,
                    ),
                ),
                ("religion", models.CharField(blank=True, max_length=30)),
                ("language", models.CharField(max_length=30)),
                ("nationality", models.CharField(max_length=30)),
            ],
        ),
    ]
