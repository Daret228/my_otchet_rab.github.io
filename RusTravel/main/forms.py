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
        }