from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username=models.CharField(max_length=250,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)
    USERNAME_FIELD='email'
    """default ma django ko user table has username in username_field but were making a overwriting/making change by using email field instead
    """
    REQUIRED_FIELDS=['password','username']
    """django ko usertable use nagari hamle custom user table use garne bhayera, we called a variable name AUTH_USER_MODEL in settings.py
    AUTH_USER_MODEL="appkoname.tablename"
    models.py lai chai call garirakhnu pardaina
    """