from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username=models.CharField(max_length=250,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=250)
    USERNAME_FIELD='email'
    """default ma django ko user table has username in username_field but were making a overwriting/making change by using email field instead
    """
    REQUIRED_FIELDS=['email','password','username']