# Generated by Django 4.1.5 on 2023-01-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cvcreator", "0002_rename_user_personaldetails"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PersonalDetails",
            new_name="PersonalInfo",
        ),
    ]
