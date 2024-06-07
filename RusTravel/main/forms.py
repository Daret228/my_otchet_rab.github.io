from .models import Account
from django.forms import ModelForm, TextInput

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Имя '
                }),

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }),

            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
                }),

            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
                })
        }