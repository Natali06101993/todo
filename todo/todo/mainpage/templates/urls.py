from django.contrib import admin
from django.urls import path
from django.urls import include  # Чтобы включать другие файлы путей!
from mainpage import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # index - это ФУНКЦИЯ в файле views - тоже сама не вырастет
    path('tasklist/', include('tasklist.urls')),
    path('mainpage/', include('tasklist.urls')),

]
