# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from .forms import OwnerForm, CarForm, ParkingForm, QueryForm

from parking.models import User, Car, Parking


def index(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        formcar = CarForm(request.POST)
        formparking = ParkingForm(request.POST)
        if form.is_valid() and formcar.is_valid() and formparking.is_valid():
            form.validar_rut()
            try:
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

                usuario = User(rut=rut, nombre=nombre,
                               apellido=apellido, sexo=sexo, edad=edad)
                usuario.save()

                idusuario = User.objects.filter(
                    rut=rut, nombre=nombre, apellido=apellido, sexo=sexo, edad=edad).values('iduser').last()

                car = Car(patente=patente, marca=marca, color=color,
                          chasis=chasis, idusuario_id=idusuario['iduser'])
                car.save()

                idauto = Car.objects.filter(patente=patente, marca=marca, color=color, chasis=chasis,
                                            idusuario_id=idusuario['iduser']).values('idcar').last()

                parking = Parking(numero=numero, dias=dias,
                                  idcar_id=idauto['idcar'])
                parking.save()

            except Exception as e:
                print e
            return render_to_response('parking.html', {'form': form, 'formcar': formcar, 'formparking': formparking},
                                      context_instance=RequestContext(request))
    else:
        form = OwnerForm()
        formcar = CarForm()
        formparking = ParkingForm()

    return render_to_response('parking.html', {'form': form, 'formcar': formcar, 'formparking': formparking},
                              context_instance=RequestContext(request))


def parking(request):
    if request.method == 'GET':
        try:
            form = QueryForm(request.GET)
            if form.is_valid():
                patente = form.cleaned_data['patente']
                try:
                    queryset = Parking.objects.filter(
                        idcar_id__patente=patente).values('dias')
                    if not queryset:
                        json_dict = {"status": "failed", "result": "no data"}
                    else:
                        json_dict = {"status": "success",
                                     "result": queryset[0]}
                    return render_to_response('queryparking.html', {'json_to_response': json_dict, 'form': form},
                                              context_instance=RequestContext(request))
                except Exception as e:
                    print e
        except Exception as e:
            print "entro en exception"
            print e
    else:
        form = QueryForm()
    return render_to_response('queryparking.html', {'form': form}, context_instance=RequestContext(request))
