from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    name = models.CharField(max_length=30)
    idNumber = models.IntegerField(verbose_name='ID Number', primary_key=True)
    dob = models.DateTimeField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=30, choices=(
        ('male', 'MALE'), ('female', 'FEMALE')))
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30,)
    maritalStatus = models.CharField(max_length=30, verbose_name='Marital Status' , choices=(
        ('married', 'MARRIED'), ('single', 'SINGLE')))
    religion = models.CharField(max_length=30, blank=True)
    language = models.CharField(max_length=30,)
    nationality = models.CharField(max_length=30,)

    def __str__(self):
        return self.name
