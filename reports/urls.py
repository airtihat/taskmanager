from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.report_dashboard, name='report_dashboard'),  # ✅ الدالة التي أضفناها سابقًا    path('', views.report_dashboard, name='report_dashboard'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('pending/', views.pending_tasks, name='pending_tasks'),
    path('overdue/', views.overdue_tasks, name='overdue_tasks'),
    path('all/', views.all_tasks, name='all_tasks'),
]
