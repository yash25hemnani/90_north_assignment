from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=200, name=False)

    USERNAME_FIELD = "email" # Changes the initial username field to email
    REQUIRED_FIELDS = ['username']

    
