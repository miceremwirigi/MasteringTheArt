# Generated by Django 4.1.5 on 2023-01-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cvcreator", "0005_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinfo",
            name="dob",
            field=models.DateTimeField(verbose_name="Date of Birth"),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="idNumber",
            field=models.IntegerField(
                primary_key=True, serialize=False, verbose_name="ID Number"
            ),
        ),
    ]
