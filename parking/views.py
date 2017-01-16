from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from .forms import ParkingForm

from parking.models import User

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ParkingForm(request.POST)
		if form.is_valid():
			rut = form.cleaned_data['RUT']
			nombre = form.cleaned_data['nombre']
			apellido = form.cleaned_data['apellido']
			sexo = form.cleaned_data['sexo']
			edad = form.cleaned_data['edad']
			try:
				usuario = User(rut=rut, nombre=nombre, apellido=apellido, sexo=sexo, edad=edad)
				usuario.save()
				print "paso el save"
			except Exception as e:
				print e
			return HttpResponse('buena')
	else:
		form = ParkingForm()

	return render_to_response('parking.html', {'form':form}, context_instance=RequestContext(request))
