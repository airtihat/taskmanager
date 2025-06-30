# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'  # هذا ضروري عند استخدام namespace

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='task_create'),
    path('edit/<int:task_id>/', views.edit_task, name='task_edit'),
    path('delete/<int:task_id>/', views.delete_task, name='task_delete'),
]
