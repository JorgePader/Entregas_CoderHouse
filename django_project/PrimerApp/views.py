from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PrimerApp.form import Curso_form
from PrimerApp.models import *


# Create your views here.
def inicio(request):
    return render(request,"padre.html")

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc= {"cursos":cursos}
    plantilla= loader.get_template("cursos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

def ver_profesores(request):
    profesores= Profesor.objects.all()
    dicc= {"profesores":profesores}
    plantilla= loader.get_template("profesores.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos= Alumno.objects.all()
    dicc= {"alumnos":alumnos}
    plantilla= loader.get_template("alumnos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso_form(request):
    if request.method == "POST":
        mi_form = Curso_form(request.POST)
        
        if mi_form.is_valid():
            datos_form = mi_form.cleaned_data
            curso = Curso(nombre=datos_form["nombre"],camada=datos_form["camada"])
            curso.save()
            return render(request,"alta_curso_form.html")

    return render(request,"alta_curso_form.html")

def alta_profesor_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        profesor = Profesor(nombre=nombre,apellido=apellido)
        profesor.save()
        return render(request,"alta_profesor_form.html")
    
    return render(request,"alta_profesor_form.html")

def alta_alumno_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        legajo = request.POST.get("legajo")
        alumno = Alumno(nombre=nombre,apellido=apellido,legajo=legajo)
        alumno.save()
        return render(request,"alta_alumno_form.html")
    
    return render(request,"alta_alumno_form.html")

def buscar_cursos_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        
        if cursos:
            return render(request, "buscar_cursos_form.html", {"cursos": cursos})
        else:
            return HttpResponse("No se encontraron cursos")
            
    return render(request, "buscar_cursos_form.html")

def buscar_profesores_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        
        if profesores:
            return render(request, "buscar_profesor_form.html", {"profesores": profesores})
        else:
            return HttpResponse("No se encontraron profesores")
            
    return render(request, "buscar_profesor_form.html")

def buscar_alumno_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        
        if alumnos:
            return render(request, "buscar_alumno_form.html", {"alumnos": alumnos})
        else:
            return HttpResponse("No se encontraron alumnos")
            
    return render(request, "buscar_alumno_form.html")

def login(request):
    return render(request, "login.html")

    