from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
