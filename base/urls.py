from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('matters/', views.matters, name='matters'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),

]