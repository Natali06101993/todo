from django.db import models
from datetime import datetime
                                                                                                                         
# Create your models here.
class Pokupka(models.Model):
    product = models.CharField(max_length=256, default='')  # создали поле product типа models.Charfield
    quantity= models.FloatField(max_length=256, default='')
    price = models.FloatField(max_length=256, default='')
    category= models.CharField(max_length=256, default='')
    picture = models.ImageField(upload_to='')
    
    
class Kategorii(models.Model):
    kategoriya = models.CharField(max_length=20, unique=True)  