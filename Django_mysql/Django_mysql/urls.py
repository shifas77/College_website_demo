"""
Definition of urls for Django_mysql.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
     path('', views.login_home, name='login_home'),
     path('login',views.Slogin,name='login'),
     path('profile/', views.Profile, name='profile'),
     path('upload-profile-photo/', views.upload_profile_photo, name='upload_profile_photo'),
     path('process-prompt/', views.process_prompt, name='process_prompt'),     
     
]
