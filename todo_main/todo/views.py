from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task'] #The input field name='task'
    Task.objects.create(task=task) #Create task in database
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk = pk) #first 'pk' is the field name from the database and the second 'pk' is the parameter name
    task.is_completed = True
    task.save() #save the task in the database with the update
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk = pk) #first 'pk' is the field name from the database and the second 'pk' is the parameter name
    task.is_completed = False
    task.save() #save the task in the database with the update
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        new_task = request.POST['task'] #The input field name='task'
        task.task = new_task
        task.save() #update
        return redirect('home')
    else:
        ctx = {
        'task':task
        }
    
        return render(request, 'edit_task.html', ctx)
    
def delete_task(request,pk):
    task = get_object_or_404(Task, pk = pk) #first 'pk' is the field name from the database and the second 'pk' is the parameter name
    task.delete()
    return redirect('home')


