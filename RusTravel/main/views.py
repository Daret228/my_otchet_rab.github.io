# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AccountForm


def index(request):
    error = 'Всё хорошо'
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            print(name, email, phone, password)

            if User.objects.filter(email=email).exists():
                error = 'Пользователь с таким email уже существует'
            elif User.objects.filter(username=name).exists():
                error = 'Пользователь с таким номером телефона уже существует'
            else:
                user = User.objects.create_user(username=name, password=password, email=email, phone=phone)
                user.save()
                messages.success(request, 'Регистрация успешна')
                return redirect('index')

        else:
            messages.error(request, 'Попробуйте ещё раз')
    else:
        form = AccountForm()

    return render(request, 'index.html', {'form': form, 'error': error})


def feedback(request):
    return render(request, 'feedback.html')
    


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
