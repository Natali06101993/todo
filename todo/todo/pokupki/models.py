from django.db import models
from datetime import datetime


class Task(models.Model):
    # id создастся сам!
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)
                                                                                                                         
# Create your models here.
class Pokupka(models.Model):
    product = models.CharField(max_length=256, default='')  # создали поле product типа models.Charfield
    quantity= models.FloatField(max_length=256, default='')
    price = models.FloatField(max_length=256, default='')
    category= models.CharField(max_length=256, default='')
    picture = models.ImageField(upload_to='')
    
    
class Kategorii(models.Model):
    kategoriya = models.CharField(max_length=20, unique=True)  