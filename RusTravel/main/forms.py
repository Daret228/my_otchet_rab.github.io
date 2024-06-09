# main/forms.py
from django import forms
from django.forms import TextInput, PasswordInput
from .models import Account, UsersFeedback

class UsersFeedbackForm(forms.ModelForm):
    class Meta:
        model = UsersFeedback
        fields = ['username', 'email', 'feedback']
        widgets = {
            "username": TextInput(attrs={
                'class': 'feedback-form',
                'placeholder': 'Ваше имя'
            }),
            "email": TextInput(attrs={
                'class': 'feedback-form',
                'placeholder': 'E-mail'
            }),
            "feedback": forms.Textarea(attrs={
                'class': 'feedback-form',
                'placeholder': 'Ваш отзыв'
            })
        }

class AccountFormRegister(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone', 'password']
        widgets = {
            'username': TextInput(attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "email": forms.EmailInput(attrs={
                'required': True,
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone': TextInput(attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "password": PasswordInput(attrs={
                'required': True,
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }

class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Имя',
        'type': 'text',
        'class': 'form-control',
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'placeholder': 'Пароль',
        'type': 'password',
        'class': 'form-control',
    }))