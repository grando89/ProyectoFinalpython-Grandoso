from django.db import models

# Create your models here.
class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"curso: {self.nombre} | camada:{self.camada}"


class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self) :
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email:{self.email}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    

    def __str__(self) :
        return f"Nombre: {self.nombre} | Apellido:{self.apellido} | Email:{self.email} "

class Entregas(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()


