from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()   

    def __str__(self):
        return f"Nombre: {self.nombre}, Camada: {self.camada}"

class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    #curso= models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

class Alumno(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    legajo= models.IntegerField()
    #curso= models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Legajo: {self.legajo}"
    
class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)
    
    def __str__(self):
        return f"User: {self.user} - Imagen: {self.imagen}"