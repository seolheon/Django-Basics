from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('hello/', views.index),
    path('date/', views.current_datetime),
]
