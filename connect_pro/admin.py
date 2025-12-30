from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

# Register your models here.
admin.site.register(User)