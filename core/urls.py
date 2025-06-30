# core/urls.py
from django.urls import path
from .views import home_view
from . import views


app_name = 'core'

urlpatterns = [
    path('', home_view, name='home'),
    path('settings/', views.settings_view, name='settings'),
]
