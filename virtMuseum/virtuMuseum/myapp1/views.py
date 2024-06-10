from django.shortcuts import render
from myapp1.models import gorodaGeroi
import sqlite3


def main_page(request):
    return render(request, 'mainPage.html')

def gorodaGeroi_page(request):
    all_gorodaGeroi=gorodaGeroi.objects.all()
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cities=[]
    names = cursor.execute("SELECT nameGeroi, smallGeroi, pictGeroi FROM myapp1_gorodaGeroi").fetchall()
    for result in names:
        #cities.append(CityInfo(result[0], result[1]))
        cities.append(result)
    cursor.close()
    print(cities)
    return render(request, 'gorodaGeroiPage.html', context={'cities':cities})

def gorodaSlavi_page(request):
    return render(request, 'gorodaSlaviPage.html')

def gorodaDoblesti_page(request):
    return render(request, 'gorodaDoblestiPage.html')
# Create your views here.
def memory_page(request):
    return render(request, 'memoryPage.html')

""" def Moscow_page(request):
     all_gorodaGeroi=gorodaGeroi.objects.all()
     gorodaGeroi_filtered=gorodaGeroi.objects.filter(nameGeroi="Москва")
     return render(request, 'Moscow.html', context={'dir': gorodaGeroi_filtered})

def Petersburg_page(request):
    gorodaGeroi_filtered=gorodaGeroi.objects.filter(nameGeroi="Санкт-Петербург")
    return render(request, 'Petersburg.html', context={'dir': gorodaGeroi_filtered})
def Volgograd_page(request):
    gorodaGeroi_filtered=gorodaGeroi.objects.filter(nameGeroi="Волгоград")
    return render(request, 'Volgograd.html', context={'dir': gorodaGeroi_filtered}) """
class CityInfo:
    def __init__(self, name, smallGeroi):
        self.name=name
        self.smallGeroi=smallGeroi 