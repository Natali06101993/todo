
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

 

#def index(request):
#    return HttpResponse('<h1>opiat privet</h1><h2>%s</h2>' % str(
#        (request.method, request.META)))
#    return HttpResponse('<pre>%s</pre>' % request.method)


    

def page():
    return HttpResponse('<h1>privet</h1>')

def index(request):
    return render(
        request,
        'mainpage/index.html',
        {
            'Задачи':Task.objects.all()   
        }
        
        # ( {'Категории':Shop.objects.all() })
        
    )


# def page(*a, **b):