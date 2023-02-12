from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('matters/', views.matters, name='matters'),
    path('matter_detail/<int:pk>/', views.matter_detail, name='matter_detail'),
    path('matters/matter_tasks/<str:pk>/', views.matter_tasks, name='matter_tasks'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('tasks/', views.tasks, name='tasks'),

    #Create a Task
    path('create_task/', views.create_task, name='create_task'),

]