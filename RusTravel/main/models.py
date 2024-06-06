from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    phone = models.CharField(max_length=15, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username + " " + self.email