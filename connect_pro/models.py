from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    USER_ROLE_CHOICES = [
        ('dev', 'developer'),
        ('clt', 'client'),
    ]

    email = models.EmailField(max_length=50, unique=True)
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=50, default='dev', blank=True, null=True)
