from django.urls import path
from . import views
from .views import note_list, export_notes_pdf

app_name = 'family_notes'

urlpatterns = [
    path('', views.note_list, name='list'),
    path('', note_list, name='list'),
    path('export/', views.export_notes_pdf, name='export_notes_pdf'),
    
    ]

