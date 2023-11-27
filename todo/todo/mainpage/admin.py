from django.contrib import admin

# Register your models here.
from .models import Task
from .models import Shop
from .models import *


class TaskAdmin(admin.ModelAdmin):
    #list_display = ('descpription', 'start', 'end')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Task._meta.fields if field.name != "id"]

#>>> my_list_1 = [i for i in range(25)]
#>>> print(my_list_1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


class ShopAdmin(admin.ModelAdmin):
    #list_display = ('descpription', 'start', 'end')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Shop._meta.fields if field.name != "id"]


class KategoriiAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Kategorii._meta.fields if field.name != "id"]
    
    
    
class PokupkaAdmin(admin.ModelAdmin):
    #list_display = ('descpription', 'start', 'end')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Pokupka._meta.fields if field.name != "id"]


admin.site.register(pokupki, PokupkaAdmin)




