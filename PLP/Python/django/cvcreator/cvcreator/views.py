from django.shortcuts import render, redirect

# Create your views here.

from .models import PersonalInfo
from .forms import PersonalInfoForm


# view to show members in the database
def viewMembers(request):
    members = PersonalInfo.objects.all()

    context = {
        'members': members,
    }
    return render(request, 'members.html', context)

# view to add member to database


def create(request):
    form = PersonalInfoForm()
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("members.html")

    context = {
        "form": form,
    }
    return render(request, "viewinfo.html", context)
