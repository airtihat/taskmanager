# tasks/management/commands/send_task_reminders.py

from django.core.management.base import BaseCommand
from tasks.models import Task
from django.utils import timezone
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'يرسل تذكيرات المهام حسب تاريخ التذكير المحدد'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        tasks = Task.objects.filter(reminder_date__date=now.date(), reminder_date__hour=now.hour)
        for task in tasks:
            send_mail(
                subject=f"🔔 تذكير بمهمة: {task.title}",
                message=f"لا تنسَ هذه المهمة:\n\n{task.description}",
                from_email=None,
                recipient_list=['your_email@gmail.com'],  # ✳️ اجعلها ديناميكية لاحقًا
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS(f"✔ تم إرسال تذكير: {task.title}"))
