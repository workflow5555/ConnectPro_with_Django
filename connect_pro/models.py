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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    headline = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)