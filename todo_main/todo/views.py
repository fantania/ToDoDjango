from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task'] #The input field name='task'
    Task.objects.create(task=task) #Create task in database
    return redirect('home')
