from django import forms

class ParkingForm(forms.Form):
    RUT = forms.CharField(label='RUT', max_length=12)
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=30)
    sexo = forms.CharField(label='Sexo', max_length=1)
    edad = forms.IntegerField(label='Edad')