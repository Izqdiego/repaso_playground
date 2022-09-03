from http.client import HTTPResponse
from urllib.request import Request
from django.shortcuts import render

from AppRepaso.forms import CursoForm, ProfeForm
from .models import Curso, Profesor
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso=Curso(nombre="curso creado en el ejemplo 0", comision=3)
    print("creando curso")
    curso.save()
    
    texto=f"Cursos creados"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppRepaso/inicio.html")

def cursos(request):
    return render(request, "AppRepaso/cursos.html")

def estudiantes(request):
    return render(request, "AppRepaso/estudiantes.html")

def profesores(request):
    return render(request, "AppRepaso/profesores.html")

def entregables(request):
    return render(request, "AppRepaso/entregables.html")

"""def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request, "AppRepaso/inicio.html")
    return render(request, "AppRepaso/cursoFormulario.html")"""
    
def curso(request):
    if request.method=="POST":
        formu=CursoForm(request.POST)
        print("---------------------")
        print(formu)
        print("---------------------")
        if formu.is_valid():
            informacion=formu.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppRepaso/inicio.html")    
    else:
        formulario=CursoForm()
        return render (request, "AppRepaso/curso.html", {"formulario":formulario})

def formularioProfe(request):


    if request.method=="POST":
        form=ProfeForm(request.POST)     
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe=Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request,"AppRepaso/inicio.html")
    else:
        formulario=ProfeForm()
        return render(request, "AppRepaso/formularioProfe.html", {"formulario":formulario})
    
def busquedaComision(request):
    return render(request, "AppRepaso/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comision=request.GET["comision"]
        # trae de la base de datos: del modelo "Curso" de los "objetos" filtrar los que comision sea igual a la comision que estamso buscando 
        cursos=Curso.objects.filter(comision=comision)
        return render(request, "AppRepaso/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppRepaso/busquedaComision.html", {"mensaje":"Ingrese una comision"})