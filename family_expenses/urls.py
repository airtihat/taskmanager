from django.urls import path
from . import views

app_name = 'family_expenses'  # ⚠️ هذا ضروري

urlpatterns = [
    path('', views.expense_list, name='list'),  # ⚠️ هذا الاسم مهم
]
