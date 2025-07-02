from django.urls import path
from . import views

app_name = 'sadaqa'

urlpatterns = [
    path('dashboard/', views.sadaqa_dashboard, name='dashboard'),  # تم التعديل هنا
    path('add/', views.add_donation, name='add_donation'),
    path('export/', views.export_pdf, name='export_pdf'),
]
