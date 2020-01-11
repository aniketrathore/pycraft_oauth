# Django Imports
from django.urls import path

# Views Imports
from api.views import (registration, login)

urlpatterns = [
    path("user/registration/", registration.UserRegistration.as_view()),
    path("login/", login.UserLogin.as_view())
]
