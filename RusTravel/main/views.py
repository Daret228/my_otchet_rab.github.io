# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UsersFeedback, Account
from .forms import AccountFormRegister, CustomLoginForm, UsersFeedbackForm
from django.core.mail import send_mail
from django.urls import reverse


def modal_auth(request):
    formReg = AccountFormRegister()
    formLog = CustomLoginForm()

    if request.method == 'POST':
        if "button_log" in request.POST:
            formLog = CustomLoginForm(request.POST)
            if formLog.is_valid():
                username = formLog.cleaned_data.get('username')
                password = formLog.cleaned_data.get('password')
                try:
                    account = Account.objects.get(username=username)
                    if account.check_password(password):
                        request.session['user_id'] = account.id
                        request.session['username'] = account.username
                        request.session['show_login_alert'] = True
                        return redirect('profile')
                    else:
                        messages.error(request, 'Неверное имя пользователя или пароль')
                        return HttpResponseRedirect(reverse('index'))
                except Account.DoesNotExist:
                    messages.error(request, 'Аккаунт не найден')
                    return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, 'Форма входа недействительна')
                formLog = CustomLoginForm()

        if "button_reg" in request.POST:
            formReg = AccountFormRegister(request.POST)
            if formReg.is_valid():
                formReg.save()
                messages.success(request, 'Регистрация успешна')
                username = formReg.cleaned_data.get('username')
                password = formReg.cleaned_data.get('password')
                account = Account.objects.get(username=username)
                request.session['show_register_alert'] = True
                request.session['user_id'] = account.id
                request.session['username'] = account.username
                return redirect('profile')
            else:
                messages.error(request, 'Ошибка регистрации. Попробуйте ещё раз')
                return HttpResponseRedirect(reverse('index'))

    return {'formReg': formReg, 'formLog': formLog}


def index(request):
    modal_form = modal_auth(request)
    data = {
        'formReg': modal_form['formReg'],
        'formLog': modal_form['formLog'],
    }
    return render(request, 'index.html', data)

def feedback(request):
    modal_form = modal_auth(request)
    news = UsersFeedback.objects.all()
    if request.method == 'POST':
        form = UsersFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = UsersFeedbackForm()

    data = {
        'formReg': modal_form['formReg'],
        'formLog': modal_form['formLog'],
        'news': news,
        'form': form
    }

    return render(request, 'feedback.html', data)

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    modal_form = modal_auth(request)
    data = {
    'formReg': modal_form['formReg'],
    'formLog': modal_form['formLog'],
    }
    return render(request, 'about.html', data)

def help_view(request):
    modal_form = modal_auth(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Сообщение от {email}\n\n{message}"

        send_mail(
            subject,
            full_message,
            'levaborisixin@gmail.com',  
            ['lev.it.up0@gmail.com'],  
            fail_silently=False,
        )

        messages.success(request, 'Ваше сообщение было отправлено!')
        return HttpResponseRedirect(reverse('send_help_email') + '?success=1')

    data = {
        'formReg': modal_form['formReg'],
        'formLog': modal_form['formLog'],
    }

        
    return render(request, 'help.html', data)