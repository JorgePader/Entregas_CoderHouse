from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PrimerApp.form import *
from PrimerApp.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request,"padre.html")

@login_required
def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc= {"cursos":cursos}
    plantilla= loader.get_template("cursos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
def ver_profesores(request):
    profesores= Profesor.objects.all()
    dicc= {"profesores":profesores}
    plantilla= loader.get_template("profesores.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
def ver_alumnos(request):
    alumnos= Alumno.objects.all()
    dicc= {"alumnos":alumnos}
    plantilla= loader.get_template("alumnos.html")
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
def alta_curso_form(request):
    if request.method == "POST":
        mi_form = Curso_form(request.POST)
        
        if mi_form.is_valid():
            datos_form = mi_form.cleaned_data
            curso = Curso(nombre=datos_form["nombre"],camada=datos_form["camada"])
            curso.save()
            return render(request,"alta_curso_form.html")

    return render(request,"alta_curso_form.html")

@login_required
def eliminar_curso_form(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request,"cursos.html",{"cursos":cursos})

@login_required
def modificar_curso_form(request,id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
       
        mi_form = Curso_form(request.POST)
        
        if mi_form.is_valid():
            datos_form = mi_form.cleaned_data
            curso.nombre = datos_form["nombre"]
            curso.camada = datos_form["camada"]
            curso.save()
            
            return render(request,"cursos.html",{"cursos":Curso.objects.all()})
    else:
        mi_form = Curso_form(initial={"nombre":curso.nombre,"camada":curso.camada})

    return render(request,"modificar_curso_form.html",{"form":mi_form,"curso":curso})

@login_required
def alta_profesor_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        profesor = Profesor(nombre=nombre,apellido=apellido)
        profesor.save()
        return render(request,"profesores.html",{"profesores":Profesor.objects.all()})
    
    return render(request,"alta_profesor_form.html")

@login_required
def eliminar_profesor_form(request,id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesores = Profesor.objects.all()
    return render(request,"profesores.html",{"profesores":profesores})

@login_required
def modificar_profesor_form(request,id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":

        mi_form = Profesor_form(request.POST)

        if mi_form.is_valid():
            datos_form = mi_form.cleaned_data
            profesor.nombre = datos_form["nombre"]
            profesor.apellido = datos_form["apellido"]
            profesor.save()

            return render(request,"profesores.html",{"profesores":Profesor.objects.all()})
        
    else:
        mi_form = Profesor_form(initial={"nombre":profesor.nombre,"apellido":profesor.apellido})
        
    return render(request,"modificar_profesor_form.html",{"form":mi_form,"profesor":profesor})

@login_required

def alta_alumno_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        legajo = request.POST.get("legajo")
        alumno = Alumno(nombre=nombre,apellido=apellido,legajo=legajo)
        alumno.save()

        return render(request,"alumnos.html",{"alumnos":Alumno.objects.all()})
    
    return render(request,"alta_alumno_form.html")

@login_required
def eliminar_alumno_form(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumnos = Alumno.objects.all()
    return render(request,"alumnos.html",{"alumnos":alumnos})

@login_required
def modificar_alumno_form(request,id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":

        mi_form = Alumno_form(request.POST)

        if mi_form.is_valid():
            datos_form = mi_form.cleaned_data
            alumno.nombre = datos_form["nombre"]
            alumno.apellido = datos_form["apellido"]
            alumno.legajo = datos_form["legajo"]
            alumno.save()

            return render(request,"alumnos.html",{"alumnos":Alumno.objects.all()})
        
    else:
        mi_form = Alumno_form(initial={"nombre":alumno.nombre,"apellido":alumno.apellido,"legajo":alumno.legajo})

    return render(request,"modificar_alumno_form.html",{"form":mi_form,"alumno":alumno})

@login_required
def buscar_cursos_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        
        if cursos:
            return render(request, "buscar_cursos_form.html", {"cursos": cursos})
        else:
            return HttpResponse("No se encontraron cursos")
            
    return render(request, "buscar_cursos_form.html")

@login_required
def buscar_profesores_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        
        if profesores:
            return render(request, "buscar_profesor_form.html", {"profesores": profesores})
        else:
            return HttpResponse("No se encontraron profesores")
            
    return render(request, "buscar_profesor_form.html")

@login_required
def buscar_alumno_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        
        if alumnos:
            return render(request, "buscar_alumno_form.html", {"alumnos": alumnos})
        else:
            return HttpResponse("No se encontraron alumnos")
            
    return render(request, "buscar_alumno_form.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return render(request, "padre.html", {"Mensaje":f"Bienvenido {user.username}"})
            else:
                return HttpResponse("Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INVALIDO {form}")

    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})

def register(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, "padre.html", {"Mensaje":f"Bienvenido {user.username}"})
        else:
            return HttpResponse("Formulario invalido")
    
    form = UserCreationForm()
    return render(request,"register.html",{"form":form})

@login_required
def editarPerfil(request):
    user= request.user

    if request.method == "POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            user.email= info["email"]
            user.set_password(info["password1"])
            user.save()

            return render(request,"padre.html",{"Mensaje":"Perfil editado correctamente"})
        
    else:
        form= UserEditForm(initial={"email":user.email})

    return render(request,"editarPerfil.html",{"form":form,"user":user})