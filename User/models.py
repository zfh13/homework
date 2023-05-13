import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=20, default='student')

class Task(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    deadLine = models.DateTimeField(default = datetime.datetime.now()+datetime.timedelta(hours=240))

    def is_overdue(self):
        return self.deadLine < datetime.datetime.now()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length = 30)
    studentNumber = models.CharField(max_length = 30)
class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_late = models.BooleanField(default=False)
