import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=20, default='student')

class Task(models.Model):
    title = models.CharField(max_length = 30,primary_key=True)
    content = models.TextField()
    deadLine = models.DateTimeField(default = datetime.datetime.now()+datetime.timedelta(hours=240))