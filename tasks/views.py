from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(req):
    return render(template_name='index.html', request=req)

@login_required(login_url='login')
def tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks.html', {'tasks': tasks})


@login_required(login_url='login')
def add_task(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user  # Assign the task to the logged-in user
            task.save()
            messages.success(req, "Task added successfully")
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(req, 'task_form.html', {'form': form})


@login_required(login_url='login')
def edit_task(req, pk):
    task = get_object_or_404(Task, pk=pk, user=req.user)  # Ensure only the owner can edit

    if req.method == 'POST':
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(req, f"{task.title} updated successfully")
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)

    return render(req, 'task_form.html', {'form': form})


@login_required(login_url='login')
def delete_task(req, pk):
    task = get_object_or_404(Task, pk=pk, user=req.user)  # Prevents unauthorized deletion
    task.delete()
    messages.success(req, f"{task.title} Deleted Successfully")
    return redirect('tasks')


@login_required(login_url='login')
def done(req, pk):
    task = get_object_or_404(Task, pk=pk, user=req.user)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    messages.success(req, f"Task '{task.title}' marked as {'Completed' if task.completed else 'Pending'}")
    return redirect('tasks')



