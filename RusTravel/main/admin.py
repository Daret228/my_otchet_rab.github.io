# main/admin.py
from django.contrib import admin
from main.models import Account, UsersFeedback

admin.site.register(Account)
admin.site.register(UsersFeedback)
