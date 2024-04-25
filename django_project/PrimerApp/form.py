from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Curso_form(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Profesor_form(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class Alumno_form(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    legajo = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email","password1","password2")
        help_texts = {k:"" for k in fields}
