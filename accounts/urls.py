from django.urls import path
from . import views
from .views import user_dashboard
from django.contrib.auth.views import LogoutView
from .views import send_email_reminder
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('profile/', views.profile_view, name='profile'),  
    path('reminder/', send_email_reminder, name='send_email_reminder'),
    # تأكد من إزالة السطر المكرر:
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
