from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('matters/', views.matters, name='matters'),
    path('matters/create_matter', views.create_matter, name='create_matter'),
    path('matter_detail/<int:pk>/', views.matter_detail, name='matter_detail'),
    path('matters/update_matter/<int:pk>/', views.update_matter, name='update_matter'),
    path('matters/delete_matter/<int:matter_id>/', views.delete_matter, name='delete_matter'),
    path('matter_detail/<int:pk>/tasks/', views.matter_tasks, name='matter_tasks'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('tasks/', views.tasks, name='tasks'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/update_task/<int:pk>/', views.update_task, name='update_task'),

    #Create a Task
    path('create_task/', views.create_task, name='create_task'),

]