from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude= ['user','views','active_connections','shared']
