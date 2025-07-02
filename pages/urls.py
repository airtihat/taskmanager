from django.urls import path
from . import views

app_name = 'pages'  # تحديد الـ namespace

urlpatterns = [
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
]
