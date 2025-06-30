from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'reminder_date', 'completed']
        labels = {
            'title': 'عنوان المهمة',
            'description': 'تفاصيل المهمة',
            'due_date': 'تاريخ التنفيذ',
            'reminder_date': 'تاريخ التذكير',  # ✅
            'completed': 'تمت؟',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'reminder_date': forms.DateInput(attrs={'type': 'datetime-local'}),  # ✅
        }
