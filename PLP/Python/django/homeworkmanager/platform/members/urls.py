from django.urls import path
from . import views

urlpatterns = [    
    path("login.html", views.login_user, name="login"),
]
