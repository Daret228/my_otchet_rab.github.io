# main/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Таблица для страницы с отзывами
class UsersFeedback(models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    feedback = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.username + " " + self.email

# Таблица для регистрации
class Account(models.Model):
    username = models.CharField(max_length=30, unique=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    phone = models.CharField(max_length=15, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        if not self.id:  # Только при создании нового пользователя
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username + " " + self.email