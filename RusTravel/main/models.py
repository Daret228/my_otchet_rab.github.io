from django.db import models

class UsersFeedback (models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    feedback = models.CharField(max_length=500, blank=False)
