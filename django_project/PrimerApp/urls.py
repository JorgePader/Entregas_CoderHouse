from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path('ver_cursos',views.ver_cursos, name="cursos"),
    path('alta_curso_form',views.alta_curso_form, name="alta_curso_form"),
    path('buscar_cursos_form',views.buscar_cursos_form, name="buscar_cursos_form"),
    path('modificar_curso_form/<int:id>',views.modificar_curso_form, name="modificar_curso_form"),
    path('eliminar_curso_form/<int:id>',views.eliminar_curso_form, name="eliminar_curso_form"),  

    path('ver_profesores',views.ver_profesores , name="profesores"),
    path('alta_profesor_form',views.alta_profesor_form, name="alta_profesor_form"),
    path('buscar_profesor_form',views.buscar_profesores_form, name="buscar_profesor_form"),
    path('modificar_profesor_form/<int:id>',views.modificar_profesor_form, name="modificar_profesor_form"),
    path('eliminar_profesor_form/<int:id>',views.eliminar_profesor_form, name="eliminar_profesor_form"),

    path('ver_alumnos',views.ver_alumnos, name="alumnos"),
    path('alta_alumno_form',views.alta_alumno_form, name="alta_alumno_form"),
    path('buscar_alumno_form',views.buscar_alumno_form, name="buscar_alumno_form"),
    path('modificar_alumno_form/<int:id>',views.modificar_alumno_form, name="modificar_alumno_form"),
    path('eliminar_alumno_form/<int:id>',views.eliminar_alumno_form, name="eliminar_alumno_form"),

    path('login',views.login_request, name="login_request"),
    path('logout',LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('register',views.register, name="register"),
    path('editarPerfil',views.editarPerfil, name="editarPerfil"),
]