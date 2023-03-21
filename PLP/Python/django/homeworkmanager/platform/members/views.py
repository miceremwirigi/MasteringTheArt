from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(
                request, message="Please use correct login details or register")
            return redirect("/members/login.html")
    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(
        request, message="Successfully logged out")
    return redirect("/")

def register_user(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data("username")
            password = form.cleaned_data("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, message="There was an error registering your account. Please try again")
            return redirect("/members/register")
    else:
        context = {
            "form": form,
        }
        return render(request, 'authenticate/register.html', context)
