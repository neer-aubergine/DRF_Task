from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100 , unique=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


