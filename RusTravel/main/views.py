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
            return redirect('index')
        
    #         if User.objects.filter(email=email).exists():
    #             error = 'Пользователь с таким email уже существует'
    #         elif User.objects.filter(username=name).exists():
    #             error = 'Пользователь с таким номером телефона уже существует'
    #         else:                
                
    #     else:
    #         messages.error(request, 'Попробуйте ещё раз')
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
        'form': form}
    return render(request, 'feedback.html', data)

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             password = form.cleaned_data['password']
#             password_confirm = form.cleaned_data['password_confirm']

#             if password == password_confirm:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'Пользователь с таким email уже существует')
#                 elif User.objects.filter(username=phone).exists():
#                     messages.error(request, 'Пользователь с таким номером телефона уже существует')
#                 else:
#                     user = User.objects.create_user(username=phone, password=password, email=email, first_name=name)
#                     user.save()
#                     messages.success(request, 'Регистрация успешна')
#                     return redirect('index')
#             else:
#                 messages.error(request, 'Пароли не совпадают')
#     else:
#         form = RegistrationForm()

#     return render(request, 'index.html', {'form': form})
    


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
