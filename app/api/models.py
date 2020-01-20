# Django Imports
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.IntegerField(default=0)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "user"
