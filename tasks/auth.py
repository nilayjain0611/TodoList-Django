from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username') 
        email = req.POST.get('email') 
        password = req.POST.get('password') 
        confirm_password = req.POST.get('confirm_password') 
        
        if confirm_password != password:
            messages.error(req, "Passwords do not match")
            return redirect('signup')

        if not username or not email or not password:
            messages.error(req, "All fields are required")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(req, "Username already exists, try another")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(req, "User created successfully")
        return redirect('login')

    return render(req, 'signup.html')


@csrf_protect
def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        if not username or not password:
            messages.error(req, "All fields are required")
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None: 
            messages.error(req, "Invalid username or password")
            return redirect('login')

        login(req, user)
        messages.success(req, f"{user.username} logged in")
        return redirect('tasks')

    return render(req, 'login.html')


def logout_user(req):
    logout(req)
    messages.success(req, "Logged out successfully")
    return redirect('login')