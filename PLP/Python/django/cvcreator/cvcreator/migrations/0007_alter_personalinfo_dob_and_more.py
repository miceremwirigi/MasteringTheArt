# Generated by Django 4.1.5 on 2023-01-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cvcreator", "0006_alter_personalinfo_dob_alter_personalinfo_idnumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinfo",
            name="dob",
            field=models.DateField(verbose_name="Date of Birth"),
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
    ]
