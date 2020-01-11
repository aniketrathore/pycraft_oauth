# Django Imports
from django.urls import path

# Views Imports
from api.views import (registration)

urlpatterns = [
    path("user/registration/", registration.UserRegistration.as_view())
]
