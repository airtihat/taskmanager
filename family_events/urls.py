# family_events/urls.py
from django.urls import path
from . import views

app_name = 'family_events'


urlpatterns = [
    path('', views.events_dashboard, name='family_events_dashboard'),
    path('', views.event_list, name='list'),  # ✅ هذا مهم
]
