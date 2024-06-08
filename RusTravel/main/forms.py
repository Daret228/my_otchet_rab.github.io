from django import forms
from .models import UsersFeedback, Account
from django.forms import ModelForm, Textarea, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import AuthenticationForm


class UsersFeedbackForm(ModelForm):
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

            "feedback": Textarea(attrs={
                'class': 'feedback-form',
                'placeholder': 'Ваш отзыв'
            })
        }   


class AccountFormRegister(ModelForm):
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

            "email": EmailInput(attrs={
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
        

class AccountFormLogin(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['usernameLog', 'passwordLog']
        widgets = {
            'usernameLog': TextInput(attrs={
                'placeholder': 'Имя',
                'type': 'text',
                'class': 'form-control', 
                }),

            "passwordLog": PasswordInput(attrs={
                'placeholder': 'Пароль',
                'type': 'password',
                'class': 'form-control',
                })
            }