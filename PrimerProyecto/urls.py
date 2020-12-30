"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from PrimerProyecto.views import bienvenido, hola2, Edad, momentoactual, contenidoHtml, miPrimeraPlantilla, PaseParametro, ConCargador, ConShortCut
from PrimerProyecto.views import hereda


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', bienvenido),
    path('hola2/', hola2),
    path('edad/<int:edad>', Edad),  # recibe un parametro que se pasa a entero
    path('momento/', momentoactual),
    path('datos/<nombre>/<edad>', contenidoHtml),
    path('plantilla/', miPrimeraPlantilla),
    path('parametro/', PaseParametro),
    path('cargador/', ConCargador),
    path('shortcuts/', ConShortCut),
    path('hereda/', hereda),
]
