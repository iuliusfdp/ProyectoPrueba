# -*- coding: utf-8 -*-

from django import forms
from itertools import cycle


class OwnerForm(forms.Form):
    RUT = forms.CharField(label='RUT', max_length=9)
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=30)
    sexo_eleccion = (('H', 'Hombre',), ('M', 'Mujer',))
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=sexo_eleccion)
    edad = forms.IntegerField(label='Edad', min_value=0)

    def validar_rut(self):
        cleaned_data = super(OwnerForm, self).clean()
        rut = cleaned_data.get("RUT")
        cuerpo = rut[:-1]
        verificador = rut[-1]

        def digito_verificador(cuerpo):
            reversed_digits = map(int, reversed(str(cuerpo)))
            factors = cycle(range(2, 8))
            s = sum(d * f for d, f in zip(reversed_digits, factors))
            return (-s) % 11

        if int(digito_verificador(cuerpo)) != int(verificador):
            self.add_error('RUT', 'Verifique el RUT')


class CarForm(forms.Form):
    marca = forms.CharField(label='Marca', max_length=30)
    color_eleccion = (('Verde', 'Verde'), ('Amarillo', 'Amarillo'),
                      (u'Marrón', u'Marrón'), ('Azul', 'Azul'),
                      ('Rojo', 'Rojo'), ('Gris', 'Gris'), ('Plata', 'Plata'),
                      ('Negro', 'Negro'), ('Blanco', 'Blanco'))
    color = forms.ChoiceField(choices=color_eleccion)
    patente = forms.CharField(label='Patente', max_length=6)
    chasis = forms.CharField(label='Chasis', max_length=10)


class ParkingForm(forms.Form):
    numero = forms.IntegerField(
        label=u'Número de Estacionamiento', min_value=1)
    dias = forms.IntegerField(label=u'Cantidad de días aparcado', min_value=1)


class QueryForm(forms.Form):
    patente = forms.CharField(label='Patente del auto')
