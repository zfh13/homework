from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from . import views
from .views import TaskListView

app_name = 'User'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('teacher/', views.createTask, name="teacher"),
    path('student/', TaskListView.as_view(), name='task_list'),
    path('student/<int:task_id>/', views.submitAssignment, name='submit_task'),
]