from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('matters/', views.matters, name='matters'),

]