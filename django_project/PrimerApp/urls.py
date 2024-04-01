from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path('ver_cursos',views.ver_cursos, name="cursos"),
    path('alta_curso_form',views.alta_curso_form, name="alta_curso_form"),
    path('buscar_cursos_form',views.buscar_cursos_form, name="buscar_cursos_form"),
    path('ver_profesores',views.ver_profesores , name="profesores"),
    path('alta_profesor_form',views.alta_profesor_form, name="alta_profesor_form"),
    path('buscar_profesor_form',views.buscar_profesores_form, name="buscar_profesor_form"),
    path('ver_alumnos',views.ver_alumnos, name="alumnos"),
    path('alta_alumno_form',views.alta_alumno_form, name="alta_alumno_form"),
    path('buscar_alumno_form',views.buscar_alumno_form, name="buscar_alumno_form"),
    path('login',views.login, name="login"),
]