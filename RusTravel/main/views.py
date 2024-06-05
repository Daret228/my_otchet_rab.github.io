# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password == password_confirm:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('index')
        else:
            messages.error(request, 'Пароли не совпадают')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль')
    return render(request, 'login.html')


def feedback(request):
    return render(request, 'feedback.html')