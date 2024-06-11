# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UsersFeedback, Account
from .forms import AccountFormRegister, CustomLoginForm, UsersFeedbackForm
from django.core.mail import send_mail
from django.urls import reverse


def modal_auth(request):
    formReg = AccountFormRegister()
    formLog = CustomLoginForm()

    # show_register_alert = request.session.pop('show_register_alert', False)
    # show_login_alert = request.session.pop('show_login_alert', False)

    if request.method == 'POST':
        if "button_log" in request.POST:
            formLog = CustomLoginForm(request.POST)
            print(1)
            if formLog.is_valid():
                print(2)
                username = formLog.cleaned_data.get('username')
                password = formLog.cleaned_data.get('password')
                try:
                    account = Account.objects.get(username=username)
                    if account.check_password(password):
                        print(3)
                        request.session['user_id'] = account.id
                        request.session['username'] = account.username
                        request.session['show_login_alert'] = True
                        return redirect('profile')
                    else:
                        print(4)
                except Account.DoesNotExist:
                    print(5)
        if "button_reg" in request.POST:
            formReg = AccountFormRegister(request.POST)
            if formReg.is_valid():
                formReg.save()
                messages.success(request, 'Регистрация успешна')
                request.session['show_register_alert'] = True
                return redirect('index')
            else:
                messages.error(request, 'Попробуйте ещё раз')

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
            email,
            ['levaborisixin@gmail.com']
        )

        return redirect(reverse('help'))

    data = {
        'formReg': modal_form['formReg'],
        'formLog': modal_form['formLog'],
    }

    return render(request, 'help.html', data)