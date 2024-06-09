from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    ]
