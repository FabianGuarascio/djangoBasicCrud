from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# List all tasks (Read)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})

# Create a new task (Create)
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'myapp/task_form.html', {'form': form})

# Update a task (Update)
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'myapp/task_form.html', {'form': form})

# Delete a task (Delete)
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'myapp/task_confirm_delete.html', {'task': task})