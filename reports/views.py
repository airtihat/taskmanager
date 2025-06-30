from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from tasks.models import Task
import datetime
import json

# التحقق من أن المستخدم مدير
def is_manager(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_manager)
def report_dashboard(request):
    tasks = Task.objects.all()
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()
    overdue = tasks.filter(due_date__lt=datetime.date.today(), completed=False).count()

    context = {
        'total_tasks': total,
        'completed_tasks': completed,
        'pending_tasks': pending,
        'overdue_tasks': overdue,
        'chart_data': json.dumps({
            'total': total,
            'completed': completed,
            'pending': pending,
            'overdue': overdue,
        }),
    }
    return render(request, 'reports/index.html', context)

@user_passes_test(is_manager)
def completed_tasks(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'reports/completed_tasks.html', {'tasks': tasks})

@user_passes_test(is_manager)
def pending_tasks(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'reports/pending_tasks.html', {'tasks': tasks})

@user_passes_test(is_manager)
def overdue_tasks(request):
    tasks = Task.objects.filter(due_date__lt=timezone.now(), completed=False)
    return render(request, 'reports/overdue_tasks.html', {'tasks': tasks})

@user_passes_test(is_manager)
def all_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'reports/all_tasks.html', {'tasks': tasks})
