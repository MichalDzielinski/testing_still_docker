from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.CharField(max_length=3, blank=True, null= True)
    town = models.CharField(max_length=50, blank=True, null= True)


