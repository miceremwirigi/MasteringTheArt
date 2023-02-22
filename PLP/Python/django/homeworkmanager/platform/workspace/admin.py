from django.contrib import admin

# Register your models here.
from .models import Tutor, Student, Subject, Assignment

admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assignment)
