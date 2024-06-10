"""
URL configuration for virtuMuseum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp1.views import main_page, gorodaGeroi_page, gorodaSlavi_page, gorodaDoblesti_page, memory_page
#Moscow_page, Petersburg_page, Volgograd_page
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('mainPage', main_page),
    path('gorodaGeroiPage', gorodaGeroi_page),
    path('gorodaSlaviPage', gorodaSlavi_page),
    path('gorodaDoblestiPage', gorodaDoblesti_page),
    path('memoryPage', memory_page),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    #path('Moscow', Moscow_page),
    #path('Petersburg', Petersburg_page),
    #path('Volgograd', Volgograd_page),
]
