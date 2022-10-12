from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellidoP = models.CharField(max_length=200)
    apellidoM = models.CharField(max_length=200)
    fechaNacimiento = models.CharField(max_length=200)
    correoElectronico = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    numero  = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    ciudad  = models.CharField(max_length=200)
    codigoPostal = models.CharField(max_length=200)

    def __str__(self) :
        return self.nombre