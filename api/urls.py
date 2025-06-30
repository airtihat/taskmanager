# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.api_views import TaskViewSet
from django.urls import include

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
