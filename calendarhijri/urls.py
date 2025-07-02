from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'calendarhijri'

urlpatterns = [
    # استخدام login_required لحماية المسار
path('dashboard/', views.dashboard_view, name='dashboard'),
]
