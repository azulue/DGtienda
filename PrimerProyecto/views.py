from django.http import HttpResponse
import datetime
from django.template import Template, Context
# Importar la libreria para cargar plantillas con get_template
from django.template import loader
# from django.template.loader import get_template

# Haciendo uso de ShortCuts
from django.shortcuts import render


def bienvenido(request):
    return HttpResponse("Bienvenido a la primera vista")


def hola2(request):
    return HttpResponse("<p style='color: blue'>Bienvenido en azul</p> ")


def Edad(request, edad):  # Con pase de parametros
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adulto"
    else:
        if edad >= 14:
            categoria = "Adolescente"
        else:
            categoria = "Infante"
    resultado = "<h1>La categoria de edad es: %s</h1>" % categoria
    return HttpResponse(resultado)


def momentoactual(request):
    momento = "<h1>El momento actual es {}</h1>".format(
        datetime.datetime.now().strftime("%A %d-%m-%Y %H:%M:%S"))
    return HttpResponse(momento)


def contenidoHtml(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Mi nombre es %s y tengo %s años</p>

    </body>
    </html>

    """ % (nombre, edad)
    return HttpResponse(contenido)

# Cargar plantilla


def miPrimeraPlantilla(request):
    # Abrir documento que contiene la plantilla
    plantillaExterna = open(
        "../PrimerProyecto/PrimerProyecto/templates/primeraPlantilla.html")

    # Crear el objeto tipo Template
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que se abrió
    plantillaExterna.close()
    # Crear un contexto
    contexto = Context()
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

# Cargar plantilla con Template


def PaseParametro(request):
    nombre = "alvaro zulueta"
    fecha = datetime.datetime.now()
    lista = ['Ford', 'Toyota', 'Mazda', 'Chevrolet', 'MG', 'Nissan']
    plntilla = open(
        "../PrimerProyecto/PrimerProyecto/templates/PaseParametros.html")
    template = Template(plntilla.read())
    plntilla.close()
    contexto = Context({'nombre': nombre, 'fecha': fecha, 'lista': lista})
    documento = template.render(contexto)
    return HttpResponse(documento)


# Cargar plantillas con el paquete loader.get_template
def ConCargador(request):
    nombre = "alvaro zulueta"
    fecha = datetime.datetime.now()
    lista = ['Ford', 'Toyota', 'Mazda', 'Chevrolet', 'MG', 'Nissan']
    plantilla = loader.get_template("PaseParametros.html")
    documento = plantilla.render(
        {'nombre': nombre, 'fecha': fecha, 'lista': lista})
    return HttpResponse(documento)


# Cargar plantilla haciendo uso del paquete ShortCuts
def ConShortCut(request):
    nombre = "alvaro zulueta"
    fecha = datetime.datetime.now()
    lista = ['Ford', 'Toyota', 'Mazda', 'Chevrolet', 'MG', 'Nissan']
    return render(request, "PaseParametros.html", {'nombre': nombre, 'fecha': fecha, 'lista': lista})


class persona (object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def hereda(request):
    pers1 = persona('Alvaro', 'Zulueta')
    return render(request, "plantilla_1.html", {'nombre': pers1.nombre, 'apellido': pers1.apellido})
