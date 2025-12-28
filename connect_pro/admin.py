from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)