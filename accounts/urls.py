from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import send_email_reminder
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('settings/', views.system_settings, name='system_settings'),  # ✅ أضف هذا
    path('security/', views.security_settings, name='security_settings'),
    path('change-password/', views.change_password, name='change_password'),
    path('enable-2fa/', views.enable_2fa, name='enable_2fa'),
    path('active-sessions/', views.active_sessions, name='active_sessions'),
    path('update-email/', views.update_email, name='update_email'),
    path('general-settings/', views.general_settings, name='general_settings'),  # ✅ إضافة هذا السطر

    path('users/', views.user_list, name='user_list'),
    path('profile/', views.profile_view, name='profile'),
    path('reminder/', send_email_reminder, name='send_email_reminder'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # تأكد من إزالة السطر المكرر:
    path('pending-approvals/', views.pending_approvals, name='pending_approvals'),
    path('approve-invite/<int:invite_id>/', views.approve_invite, name='approve_invite'),
    path('manage-users/', views.manage_users, name='manage_users'),  # رابط إدارة المستخدمين
    path('pending-approvals/', views.pending_approvals, name='pending_approvals'),
    path('reports/', views.reports, name='reports'),
    path('send-invite/', views.send_invite, name='send_invite'),
    path('send-reminder/', views.send_reminder, name='send_reminder'),  # تأكد من إغلاق النصوص    path('system-settings/', views.system_settings, name='system_settings'),
    path('user-list/', views.user_list, name='user_list'),
]
