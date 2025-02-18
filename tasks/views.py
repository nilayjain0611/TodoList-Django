from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(req):
    return render(template_name='index.html', request=req)

def tasks(req):
    tasks = Task.objects.all().order_by('-created_at')
    return render(req,'tasks.html', {'tasks':tasks})

def add_task(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else: 
            print('Invalud')

    else:
        form = TaskForm()  # Empty form for GET request
    return render(req,'task_form.html', {'form':form})
def edit_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if req.method == 'POST':
        form = TaskForm(req.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks')

    else:
        form = TaskForm(instance=task) 
    
    return render(req,'task_form.html',{'form':form})
def delete_task(req, pk):
    task =  get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('tasks')
    
def done(req, pk):
    
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        
        task.save()
    
        return redirect('tasks')



