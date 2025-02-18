from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(req):
    return render(template_name='index.html', request=req)

@login_required(login_url='login')
def tasks(request):
    task = None
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('created_at')
    else:
        tasks = None
        return redirect('login')
    return render(request,'tasks.html', {'tasks':tasks})
        
@login_required(login_url='login')
def add_task(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('tasks')
        else: 
            print('Invalid')

    else:
        form = TaskForm()  
    return render(req,'task_form.html', {'form':form})

@login_required(login_url='login')
def edit_task(req, pk):
    if req.user.is_authenticated:
        task = get_object_or_404(Task, pk=pk)
        
        if req.method == 'POST':
            form = TaskForm(req.POST, instance=task)

            if form.is_valid():
                
                form.save()
                return redirect('tasks')

        else:
            form = TaskForm(instance=task) 
    else: 
        task = None
        return redirect('login')
    
    
    return render(req,'task_form.html',{'form':form})

@login_required(login_url='login')
def delete_task(req, pk):
    task =  get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('tasks')
    
@login_required(login_url='login')
def done(req, pk):
    
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        
        task.save()
    
        return redirect('tasks')



