import datetime

import django
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import User, Task


# 注册视图函数
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        User.objects.create(username=username, email=email,password=password,role=role)
        return redirect("User:login")
    return render(request, 'User/register.html')

def home(request):
    return render(request, 'User/home.html')

# 登录视图函数
def login(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'teacher':
            return redirect('User:teacher')
        if role == 'student':
            return redirect('User:student')
    return render(request, 'User/login.html', {})

def createTask(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        deadLine = request.POST.get("deadLine")
        task = Task()
        task.title = title
        task.content = content
        task.deadLine = deadLine
        task.save()
    return render(request, 'User/teacher.html')

def upload(request):

    return render(request, 'User/upload.html')

def past_homework(task):
    return task.deadLine <= datetime.datetime.now()

class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'User/student.html'



