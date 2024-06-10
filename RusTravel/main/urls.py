from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('help/', views.help_view, name='help'),
    path('send_help_email/', views.help_view, name='send_help_email'),
    ]
