from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso=Curso(nombre="AWS", comision=3)
    curso2=Curso(nombre="Lengua", comision=1)
    curso3=Curso(nombre="Matematica", comision=2)
    curso.save()
    curso2.save()
    curso3.save()
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

