from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


# ✅ عرض قائمة المهام
@login_required
def task_list(request):
    status = request.GET.get('status')
    if status == 'completed':
        tasks = Task.objects.filter(created_by=request.user, completed=True)
    elif status == 'pending':
        tasks = Task.objects.filter(created_by=request.user, completed=False)
    else:
        tasks = Task.objects.filter(created_by=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# ✅ إنشاء مهمة جديدة
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# ✅ تعديل مهمة
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/create_task.html', {'form': form, 'edit_mode': True})

# ✅ حذف مهمة
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})
