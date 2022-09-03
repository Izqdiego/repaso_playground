from msilib.schema import Patch
from django.urls import path
from AppRepaso.views import *


urlpatterns = [
    path('curso/', curso),
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('curso/', curso, name="curso"),
    path('formularioProfe/', formularioProfe, name="formularioProfe"),
    path('busquedaComision/', busquedaComision, name="busquedacomision"),
    path('buscar/', buscar, name="buscar")
]