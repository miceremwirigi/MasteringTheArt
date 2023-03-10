# Generated by Django 4.1.5 on 2023-01-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cvcreator", "0008_alter_personalinfo_dob_alter_personalinfo_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinfo",
            name="dob",
            field=models.DateField(
                help_text="Please use the following format: YYYY-MM-DD",
                verbose_name="Date of Birth",
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="gender",
            field=models.CharField(
                choices=[("male", "MALE"), ("female", "FEMALE")], max_length=30
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="idNumber",
            field=models.IntegerField(
                help_text="National ID or Passport number",
                primary_key=True,
                serialize=False,
                verbose_name="ID Number",
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="maritalStatus",
            field=models.CharField(
                choices=[("married", "MARRIED"), ("single", "SINGLE")],
                max_length=30,
                verbose_name="Marital Status",
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="name",
            field=models.CharField(help_text="Please Enter full name", max_length=30),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="religion",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="telephone",
            field=models.CharField(
                help_text="Beginn with country code, e.g. +254734323443", max_length=30
            ),
        ),
    ]
