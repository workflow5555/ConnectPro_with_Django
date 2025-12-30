from django.db import models
from connect_pro.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,default='')
    headline = models.CharField(max_length=100,default='')
    bio = models.TextField(default='')
    profile_pic = models.ImageField(upload_to='profile_pics', default='profile_pics/avatar.svg')
    location = models.CharField(max_length=50,default='')
    views = models.IntegerField(default=0)
    active_connections = models.IntegerField(default=100)
    shared = models.BooleanField(default=False)