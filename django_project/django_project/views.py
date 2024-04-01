# las vistas son funciones que reciben una peticion y devuelven una respuesta, se crean en el archivo views.py

from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("<h1>Hola, mundo!</h1>")

def majority_age(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")
    
def template(request):
    mi_html= open("C:/#Facultad/Coder_CursoPython/Practicas/proyecto_django/django_project/django_project/pantillas/template.html")
    plantilla= Template(mi_html.read())
    mi_html.close()

    mi_contexto= Context({"nombre": "Juan"})

    documento= plantilla.render(mi_contexto)
    return HttpResponse(documento)
