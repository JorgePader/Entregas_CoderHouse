from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()   

class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    #curso= models.ForeignKey(Curso, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    legajo= models.IntegerField()
    #curso= models.ForeignKey(Curso, on_delete=models.CASCADE)