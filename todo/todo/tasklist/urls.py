from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # index - это ФУНКЦИЯ в файле views - тоже сама не вырастет
]
