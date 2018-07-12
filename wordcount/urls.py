from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'), # name of function in views.py
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about')
]
