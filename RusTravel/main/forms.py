<<<<<<< HEAD
from .models import UsersFeedback
from django.forms import ModelForm, Textarea, TextInput



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
=======
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
>>>>>>> 8169530c22626ed0336631c10cbc5187b30d977e
        }