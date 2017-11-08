from django.db import models
from django.contrib import admin
# Create your models here.
class Vehiculos(models.Model):

    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    placa = models.CharField(max_length=30)

    def __str__(self):

       return self.placa

class Parqueo(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_inicial = models.DateField()
    fecha_salida = models.DateField()
    transportes = models.ManyToManyField(Vehiculos,through='Tipos')

    def __str__(self):

       return self.nombre


class Tipos(models.Model):

    parqueo = models.ForeignKey(Parqueo, on_delete=models.CASCADE)
    vehiculos= models.ForeignKey(Vehiculos, on_delete=models.CASCADE)

class TiposInLine(admin.TabularInline):

    model = Tipos

class ParqueoAdmin(admin.ModelAdmin):

    inlines = (TiposInLine,)


class VehiculosAdmin (admin.ModelAdmin):

    inlines = (TiposInLine,)
