from django.shortcuts import render
from .models import *


# Create your views here.


def get_menu(active):
    result = []
    for elem in todo.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result







def index(request):
    result = ""

    kateg = ""
    for a in Kategorii.objects.all():
        kateg += a.kategoriya

    

def pokupki(request):

    result = ""

    tovary = ""
    for x in Pokupka.objects.all():
        tovary += x.namegoods

    return render(
        request,
        "pokupki/index2.html",

        # Kонтекст передаваемых переменных
        {

            "Товары": Pokupka.objects.all(),
            "navset": get_menu("/shopping")

        }
    )