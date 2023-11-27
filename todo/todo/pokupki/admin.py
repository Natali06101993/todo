from django.contrib import admin
from .models import *





class TaskAdmin(admin.ModelAdmin):
    #list_display = ('descpription', 'start', 'end')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Task._meta.fields if field.name != "id"]
    
    

# Register your models here.
class PokupkaAdmin(admin.ModelAdmin):
    #list_display = ('descpription', 'start', 'end')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Pokupka._meta.fields if field.name != "id"]


admin.site.register(Pokupka, PokupkaAdmin)





class KategoriiAdmin(admin.ModelAdmin):
     list_display = [
        field.name for field in Kategorii._meta.fields if field.name != "id"]
     
admin.site.register(Kategorii, KategoriiAdmin)   
   
 
