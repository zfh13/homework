import datetime

import django
from django.contrib.auth.decorators import login_required
from django.core.checks import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from .form import DocumentForm, SubmissionForm
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
        role = request.POST.get('role')
        if role == 'teacher':
            return redirect('User:teacher')
        if role == 'student':
            return HttpResponseRedirect("/student/")
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

class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'User/student.html'



class SubmissionView(FormView):
    form_class = SubmissionForm
    template_name = 'User/upload.html'
    success_url = reverse_lazy('task_list')


    def form_valid(self, form):
        # 保存提交信息
        task_id = self.kwargs['task_id']
        task = get_object_or_404(Task, pk=task_id)
        name = self.request.POST.get("name")
        studentNumber = self.request.POST.get("studentNumber")
        student = Student(name=name,studentNumber=studentNumber)
        file = form.cleaned_data['file']
        submission = Submission(task=task, student=student, file=file)
        submission.save()

        # 判断是否逾期
        if datetime.timezone.now() > task.deadLine:
            submission.is_late = True
            submission.save()
            messages.warning(self.request, '任务已经逾期')
        else:
            messages.success(self.request, '任务提交成功')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs