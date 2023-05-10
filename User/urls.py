from django.urls import path, include
from . import views

app_name = 'User'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('teacher/', views.createTask, name="teacher"),
    path('student/', views.TaskListView.as_view(), name="tasklist"),
    path('upload/', views.upload, name="upload")
]