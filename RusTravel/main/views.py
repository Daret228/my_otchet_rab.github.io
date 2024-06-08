# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UsersFeedback
from .forms import AccountFormRegister, AccountFormLogin, UsersFeedbackForm
from django.contrib.auth import authenticate, login

def index(request):
    formReg = AccountFormRegister()
    formLog = AccountFormLogin()

    #Проверка на Post запрос
    if request.method == 'POST':
    
        #Проверка на нажатие кнопки авторизации
        if "button_log" in request.POST:
            formLog = AccountFormLogin(request.POST)
            if formLog.is_valid():
                username = formLog.cleaned_data['usernameLog']
                password = formLog.cleaned_data['passwordLog']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('index')
            else:
                messages.error(request, 'Неправильное имя пользователя или пароль')
        
        #Проверка на нажатие кнопки регистрации
        if "button_reg" in request.POST:
            formReg = AccountFormRegister(request.POST)
            if formReg.is_valid():
                formReg.save()
                messages.success(request, 'Регистрация успешна')
                return redirect('index')
                
            else:
                messages.error(request, 'Попробуйте ещё раз')
    else:
        formReg = AccountFormRegister()
        formLog = AccountFormLogin()
    
    data = {
        'formReg': formReg,
        'formLog': formLog
    }
    print(data)
    return render(request, 'index.html', data)


#Функция для обработки отзывов
def feedback(request):
    news=UsersFeedback.objects.all()
    if request.method == 'POST':
        form = UsersFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = UsersFeedbackForm()

    data = {
    'news': news,
    'form': form
    }

    return render(request, 'feedback.html', data)