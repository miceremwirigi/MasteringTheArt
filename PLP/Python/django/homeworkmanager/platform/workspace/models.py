from django.db import models

# Create your models here.


class Tutor(models.Model):
    first_name = models.CharField(max_length=60, blank=False, editable=True)
    last_name = models.CharField(max_length=60, blank=False, editable=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    first_name = models.CharField(
        max_length=60, blank=False, editable=True, verbose_name="First Name")
    last_name = models.CharField(
        max_length=60, blank=False, editable=True, verbose_name="Last Name")
    reg_no = models.CharField(
        max_length=60, blank=False, verbose_name="Registration Number", default="REG")
    tutor = models.ManyToManyField(Tutor, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subject(models.Model):
    subject = models.CharField(max_length=60, blank=False,
                            editable=True, default="Subject", primary_key=True)
    tutor = models.ManyToManyField(Tutor)
    student = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.subject


class Assignment(models.Model):
    topic = models.CharField(max_length=60, blank=False, editable=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, default="subject")
    discription = models.TextField(blank=True)
    due_date = models.DateTimeField(
        blank=False, editable=True, verbose_name="Due Date")
    student = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.subject.subject + ":  " + self.topic
