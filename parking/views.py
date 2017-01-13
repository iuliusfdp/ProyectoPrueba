from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

from .forms import ParkingForm

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ParkingForm(request.POST)
		if form.is_valid():
			return HttpResponse('buena')
	else:
		form = ParkingForm()

	return render_to_response('parking.html', {'form':form}, context_instance=RequestContext(request))