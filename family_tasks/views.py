# استيراد النموذج والمكتبة المطلوبة
from django.shortcuts import render, redirect
from .forms import FamilyTaskForm
from .models import FamilyTask


# دالة لإضافة مهمة جديدة
def add_task(request):
    if request.method == 'POST':
        form = FamilyTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_tasks:task_list')
    else:
        form = FamilyTaskForm()
    return render(request, 'family_tasks/add_task.html', {'form': form})

# ✅ دالة لعرض قائمة المهام
def task_list(request):
    tasks = FamilyTask.objects.all()
    return render(request, 'family_tasks/task_list.html', {'tasks': tasks})
