from django.urls import path
from . import views
from .views import add_task, task_list  # ✅ هنا فقط

app_name = 'family_tasks'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('add/', views.add_task, name='add'),
    path('add/', views.add_task, name='add_task'),
    path('', views.task_list, name='task_list'),  # هذا هو المطلوب
]
