from django.urls import path
from . import views
from .views import family_dashboard

app_name = 'family'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
