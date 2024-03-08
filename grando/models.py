from django.db import models

# Create your models here.
class Bebida_blanca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"nombre: {self.nombre} | cantidad:{self.cantidad}"


class Vinos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self) :
        return f"Nombre: {self.nombre} | Cantidad: {self.cantidad}"

class Bebida_sa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self) :
        return f"Nombre: {self.nombre} | Cantidad: {self.cantidad}"

class Entregas(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()


