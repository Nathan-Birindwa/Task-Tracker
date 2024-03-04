from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("Login", views.Login, name="Login")
]

