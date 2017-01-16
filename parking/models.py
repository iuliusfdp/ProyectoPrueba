from django.db import models
from django.db.models.fields.related import ForeignKey

class User(models.Model):
	iduser = models.AutoField(primary_key=True)
	rut = models.CharField(max_length=12)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	sexo = models.CharField(max_length=1)
	edad = models.IntegerField()

class Car(models.Model):
	idcar = models.AutoField(primary_key=True)
	patente = models.CharField(max_length=6)
	marca = models.CharField(max_length=30)
	color = models.CharField(max_length=20)
	chasis = models.CharField(max_length=10)
	idusuario = models.ForeignKey(User)

class Parking(models.Model):
	idparking = models.AutoField(primary_key=True)
	numero = models.IntegerField()
	dias = models.IntegerField()
	idcar = models.ForeignKey(Car)
