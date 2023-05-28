import datetime

from django.core.checks import messages

from django.http import HttpResponse, HttpResponseRedirect



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from . import models
from .form import DocumentForm, SubmissionForm, UserFormLogin
from .models import User, Task, Submission, Student


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
        obj_user = UserFormLogin(request.POST)
        if obj_user.is_valid():
            username = obj_user.cleaned_data['username']
            password = obj_user.cleaned_data['password']
            userResult = User.objects.filter(username=username, password=password)
            if len(userResult) <= 0:
                return HttpResponse("该用户不存在")
            role = request.POST.get('role')
            if role == 'teacher':
                return redirect('User:teacher')
            if role == 'student':
                return HttpResponseRedirect("/student/")
    return render(request, 'User/login.html')

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



def submitAssignment(request,task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        name = request.POST.get("name")
        studentNumber = request.POST.get("studentNumber")
        student = Student.objects.create(name=name,studentNumber=studentNumber)
        file = request.POST.get("file")
        submission = Submission(student=student, task=task,file=file)
        datenow = datetime.datetime.now().replace(tzinfo=None)
        deadline = submission.task.deadLine.replace(tzinfo=None)
        if datenow > deadline:
            return HttpResponse("作业已经超时")
        submission.save()
    return render(request, 'User/upload.html')

class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'User/student.html'


