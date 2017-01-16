from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.

class User(models.Model):
	rut = models.CharField(primary_key=True, max_length=12)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	sexo = models.CharField(max_length=1)
	edad = models.IntegerField()