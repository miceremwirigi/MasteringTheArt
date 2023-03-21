from django.urls import path
from . import views

urlpatterns = [    
    path("login.html", views.login_user, name="login"),
    path("logout.html", views.logout_user, name="logout"),
    path("register.html", views.register_user, name="register_user"),
]
