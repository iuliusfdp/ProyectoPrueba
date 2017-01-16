# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from .forms import OwnerForm, CarForm, ParkingForm

from parking.models import User, Car, Parking


def index(request):
	if request.method == 'POST':
		form = OwnerForm(request.POST)
		formcar = CarForm(request.POST)
		formparking = ParkingForm(request.POST)
		if form.is_valid() and formcar.is_valid() and formparking.is_valid():
			rut = form.cleaned_data['RUT']
			nombre = form.cleaned_data['nombre']
			apellido = form.cleaned_data['apellido']
			sexo = form.cleaned_data['sexo']
			edad = form.cleaned_data['edad']

			marca = formcar.cleaned_data['marca']
			color = formcar.cleaned_data['color']
			patente = formcar.cleaned_data['patente']
			chasis = formcar.cleaned_data['chasis']

			numero = formparking.cleaned_data['numero']
			dias = formparking.cleaned_data['dias']

			try:
				usuario = User(rut=rut, nombre=nombre, apellido=apellido, sexo=sexo, edad=edad)
				usuario.save()

				idusuario = User.objects.filter(rut=rut, nombre=nombre, apellido=apellido, sexo=sexo, 
					edad=edad).values('iduser').last()

				car = Car(patente=patente, marca=marca, color=color, chasis=chasis, idusuario_id=idusuario['iduser'])
				car.save()

				idauto = Car.objects.filter(patente=patente, marca=marca, color=color, chasis=chasis, 
					idusuario_id=idusuario['iduser']).values('idcar').last()

				parking = Parking(numero=numero, dias=dias, idcar_id=idauto['idcar'])
				parking.save()

			except Exception as e:
				print e
			return HttpResponse('buena')
	else:
		form = OwnerForm()
		formcar = CarForm()
		formparking = ParkingForm()

	return render_to_response('parking.html', {'form':form, 'formcar':formcar, 'formparking':formparking}, 
		context_instance=RequestContext(request))
