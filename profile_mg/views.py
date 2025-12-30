from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from profile_mg.models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import base64
from django.core.files.base import ContentFile
from .forms import ProfileUpdateForm
from connect_pro.forms import UserForm
# Create your views here.



def profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile is None:
            user_profile = UserProfile(user=request.user)
            user_profile.save()

        return render(request, 'profile/profile.html',{'user_profile':user_profile})

    return redirect('login')

@login_required(login_url='/login')
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileUpdateForm(instance=user_profile)
    return render(request,'profile/profile_edit.html',{'form':form})

@login_required(login_url='/login/')
def share_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.shared = True
    user_profile.save()
    return redirect('view_profile')