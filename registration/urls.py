from django.contrib import admin
from django.urls import path
from .views import login, logout, register

urlpatterns=[
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
]