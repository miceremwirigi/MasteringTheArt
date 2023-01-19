from django.shortcuts import render, redirect

# Create your views here.

from .models import PersonalInfo
from .forms import PersonalInfoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from docx import *
from docx.shared import Inches


# view to show members in the database
def viewMembers(request):
    members = PersonalInfo.objects.all()

    context = {
        'members': members,
    }
    return render(request, 'home.html', context)

# view to add member to database


def createnewinfo(request):
    form = PersonalInfoForm()
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("/"))

    context = {
        "form": form,
    }
    return render(request, "createnewinfo.html", context)


def createDoc(request):
    document = Document()
    document_title = "CV.docx"
