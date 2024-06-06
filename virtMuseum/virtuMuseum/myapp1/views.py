from django.shortcuts import render
from myapp1.models import gorodaGeroi
import sqlite3


def main_page(request):
    return render(request, 'mainPage.html')

def gorodaGeroi_page(request):
    all_gorodaGeroi=gorodaGeroi.objects.all()
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()

    names = cursor.execute("SELECT name FROM myapp1_gorodaGeroi").fetchall()

    cursor.close()
    print(names)


    return render(request, 'gorodaGeroiPage.html', context={'names':names})

def gorodaSlavi_page(request):
    return render(request, 'gorodaSlaviPage.html')

def gorodaDoblesti_page(request):
    return render(request, 'gorodaDoblestiPage.html')
# Create your views here.
def memory_page(request):
    return render(request, 'memoryPage.html')