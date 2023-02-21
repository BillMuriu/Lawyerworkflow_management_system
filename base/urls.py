from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #Matters
    path('matters/', views.matters, name='matters'),
    path('matters/create_matter', views.create_matter, name='create_matter'),
    path('matter_detail/<int:pk>/', views.matter_detail, name='matter_detail'),
    path('matters/update_matter/<int:pk>/', views.update_matter, name='update_matter'),
    path('matters/delete_matter/<int:matter_id>/', views.delete_matter, name='delete_matter'),
    path('matter_detail/<int:pk>/tasks/', views.matter_tasks, name='matter_tasks'),


    #Login and Register
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    

    #Tasks
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

]