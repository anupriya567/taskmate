from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# .forms k mtlb forms iise same directory m h ya isse same folder m h

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()            
        messages.success(request,("New task added!"))
        return redirect('todolist')    
    else:
        all_tasks = TaskList.objects.filter(manager = request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html',{'all_tasks':all_tasks})

def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.manager == request.user):
        task.delete()
    else:
        messages.error(request,("Access Denied! You can't delete this "))   
    return redirect('todolist')

def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.manager == request.user):
        task.done = True
        task.save()
    else:
        messages.error(request,("Access Denied! You can't change this "))    
    return redirect('todolist') 

def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.manager == request.user):
        task.done = False
        task.save()
    else:
        messages.error(request,("Access Denied! You can't change this "))      
    return redirect('todolist')   
    
def edit_task(request,task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,(" task edited!"))
        return redirect('todolist')   
    else:
        task_obj = TaskList.objects.get(pk=task_id)  
        return render(request, 'edit.html',{'task_obj':task_obj})

def index(request):

    context = {'index_text':"Hello, world! index is here",
              }
    return render(request, 'index.html',context)

@login_required
def about(request):

    context = {'about_text':"Hello, world! about is here",
              }
    return render(request, 'about.html',context)

@login_required
def contact(request):

    context = {'contact_text':"Hello, world! contact is here",
              }
    return render(request, 'contact.html',context)