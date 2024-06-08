# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AccountForm, UsersFeedbackForm


def index(request):
    error = 'Всё хорошо'
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна')
            form.save()
            return redirect('index')
            
        else:
            messages.error(request, 'Попробуйте ещё раз')
    else:
        form = AccountForm()

    return render(request, 'index.html', {'form': form, 'error': error})


def feedback(request):
    error= ''

    if request.method == 'POST':
        form = UsersFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else: 
            error = 'Введены неверные данные: имя пользователя или e-mail'

    form = UsersFeedbackForm()

    data = {
        'form': form,
        'error': error}
    
    return render(request, 'feedback.html', data)


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, 'Неправильное имя пользователя или пароль')
#     return render(request, 'index.html')
