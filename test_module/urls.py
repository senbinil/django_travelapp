from django.contrib import admin
from django.urls import path
from .views import  demo,about

urlpatterns=[
    path('',demo,name='home'),
    path('about',about,name='about'),
    # path('add',add,name="add")
]