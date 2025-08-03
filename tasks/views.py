from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def task_list(request):
    """
    READ operation - Display all tasks
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'title': 'All Tasks'
    }
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    """
    CREATE operation - Create a new task
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'title': 'Create New Task',
        'button_text': 'Create Task'
    }
    return render(request, 'tasks/task_form.html', context)


def task_detail(request, pk):
    """
    READ operation - Display single task details
    """
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
        'title': f'Task: {task.title}'
    }
    return render(request, 'tasks/task_detail.html', context)


def task_update(request, pk):
    """
    UPDATE operation - Update existing task
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save()
            messages.success(request, f'Task "{updated_task.title}" updated successfully!')
            return redirect('task_detail', pk=updated_task.pk)
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
        'title': f'Update: {task.title}',
        'button_text': 'Update Task'
    }
    return render(request, 'tasks/task_form.html', context)


def task_delete(request, pk):
    """
    DELETE operation - Delete a task
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" deleted successfully!')
        return redirect('task_list')

    context = {
        'task': task,
        'title': f'Delete: {task.title}'
    }
    return render(request, 'tasks/task_confirm_delete.html', context)