from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from profile_mg.models import UserProfile
from django.contrib import messages
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Email does not exist')
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/profile/')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login/login.html')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        username = full_name.replace(" ","").lower()
        role = request.POST.get('role')
        print(full_name,email,password,role,username)
        try:
            user = User.objects.get(email=email)
            messages.error(request, 'Email already exists')
        except User.DoesNotExist:
            user = User.objects.create_user(email=email,username=username, password=password, role=role)
            userprofile = UserProfile.objects.create(user=user, full_name=full_name)
            login(request, user)
            messages.success(request, 'Account created for ' + full_name)
            return redirect('/profile/')
    return  render(request, 'login/signup.html')
