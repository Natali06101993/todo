from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)

class Shop(models.Model):# механизм наследования
    category = models.CharField(max_length=256, default='')#котегории
    description = models.CharField(max_length=256, default='')#описание
    

    

    