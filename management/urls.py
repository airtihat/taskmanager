# management/urls.py
from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('settings/', views.settings_view, name='settings'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
