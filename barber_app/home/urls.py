from django.urls import path
from .views import *

urlpatterns = [
    path("", main, name="home"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    
]