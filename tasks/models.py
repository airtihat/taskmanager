from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان المهمة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    due_date = models.DateTimeField(verbose_name="تاريخ التسليم")
    reminder_date = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ التذكير")  # 🔔
    completed = models.BooleanField(default=False, verbose_name="تمت؟")  # ✅ ضفناها هنا
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    