# Django Imports
from django.urls import path

# Views Imports
from api.views import (registration, login, profile, logout)

urlpatterns = [
    path("user/registration/", registration.UserRegistration.as_view()),
    path("user/profile", profile.UserProfileDetails.as_view()),
    path("login/", login.UserLogin.as_view()),
    path("logout/", logout.UserLogOut.as_view())
]
