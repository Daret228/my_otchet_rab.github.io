from .models import Account
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput

class AccountForm(ModelForm):
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