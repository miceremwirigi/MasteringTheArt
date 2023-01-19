from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    name = models.CharField(max_length=30, help_text="Please Enter full name")
    idNumber = models.IntegerField(
        verbose_name='ID Number', primary_key=True, help_text="National ID or Passport number")
    dob = models.DateField(verbose_name='Date of Birth',
                           help_text="Please use the following format: YYYY-MM-DD")
    gender = models.CharField(max_length=30, choices=(
        ('male', 'MALE'), ('female', 'FEMALE')), help_text="")
    email = models.EmailField(blank=True, help_text="")
    telephone = models.CharField(max_length=30, help_text="Beginn with country code, e.g. +254734323443")
    maritalStatus = models.CharField(max_length=30, verbose_name='Marital Status' , choices=(
        ('married', 'MARRIED'), ('single', 'SINGLE')), help_text="")
    religion = models.CharField(max_length=30, blank=True, help_text="")
    language = models.CharField(max_length=30, help_text="What languages can you speak")
    nationality = models.CharField(max_length=30, help_text="What's your nationality?")

    def __str__(self):
        return self.name
