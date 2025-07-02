from django import forms
from .models import FamilyTask  # افترض أن اسم النموذج هو FamilyTask

class FamilyTaskForm(forms.ModelForm):
    class Meta:
        model = FamilyTask
        fields = ['title', 'description', 'due_date']  # عدل حسب الحقول الموجودة لديك
        labels = {
            'title': 'عنوان المهمة',
            'description': 'تفاصيل المهمة',
            'due_date': 'تاريخ الاستحقاق',
        }
