# -*- coding: utf-8 -*-

from django import forms

class OwnerForm(forms.Form):
    RUT = forms.CharField(label='RUT', max_length=12)
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=30)
    sexo = forms.CharField(label='Sexo', max_length=1)
    edad = forms.IntegerField(label='Edad')


class CarForm(forms.Form):
	marca = forms.CharField(label='Marca', max_length=30)
	color = forms.CharField(label='Color', max_length=20)
	patente = forms.CharField(label='Patente', max_length=6)
	chasis = forms.CharField(label='Chasis', max_length=10)


class ParkingForm(forms.Form):
	numero = forms.IntegerField(label=u'Número de Estacionamiento')
	dias = forms.IntegerField(label=u'Cantidad de días aparcado')


class QueryForm(forms.Form):
	patente = forms.CharField(label='Patente del auto')