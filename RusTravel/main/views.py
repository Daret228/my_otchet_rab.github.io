from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UsersFeedback, Account
from .forms import AccountFormRegister, CustomLoginForm, UsersFeedbackForm


def index(request):
    formReg = AccountFormRegister()
    formLog = CustomLoginForm()

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

    data = {
        'formReg': formReg,
        'formLog': formLog,
    }
    return render(request, 'index.html', data)

def feedback(request):
    news = UsersFeedback.objects.all()
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

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'profile.html')