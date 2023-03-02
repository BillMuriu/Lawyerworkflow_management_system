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

    #Events

    path('events/', views.events, name='events'),
    path('create_event/', views.create_event, name='create_event'),
    path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),


    #Documents
    path('create_document/', views.create_document, name='create_document'),
    path('document_detail/<int:document_id>/', views.document_detail, name='document_detail'),


    #Notes
    path('create_note/', views.create_note, name='create_note'),
    path('note_detail/<int:note_id>/', views.note_detail, name='note_detail'),


    #IndividualClient
    path('create_individual_client/', views.create_individual_client, name='create_individual_client'),
    path('individual_client_detail/<int:client_id>/', views.individual_client_detail, name='individual_client_detail'),


    #BusinessClient
    path('create_business_client/', views.create_business_client, name='create_business_client'),
    path('business_client_detail/<int:client_id>/', views.business_client_detail, name='business_client_detail'),


    #Feenote
    path('create_feenote/', views.create_feenote, name='create_feenote'),
    path('feenote_detail/<int:feenote_id>/', views.feenote_detail, name='feenote_detail'),

]