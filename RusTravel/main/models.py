from django.db import models

# Таблица для страницы с отзывами
class UsersFeedback (models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    feedback = models.CharField(max_length=500, blank=False)


# Таблица для регистрации
class Account(models.Model):
    username = models.CharField(max_length=30, unique=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    phone = models.CharField(max_length=15, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username + " " + self.email