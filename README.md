# ProyectoPrueba

Tutorial para Proyecto Prueba en Django.

El siguiente proyecto trata sobre la implementación de un registro de automóviles en un estacionamiento.

Views
=========

- Index: Función inicial que almacena mediante un formulario los datos del propietario del auto, los datos del auto y los datos del estacionamiento.
- Parking: Función que consulta la cantidad de días que ha estado aparcado un auto según su número de patente.

Forms
=========

- OwnerForm: Formulario para completar los datos del propietario del vehículo.
- CarForm: Formulario para completar los datos del vehículo.
- ParkingForm: Formulario para completar los datos del estacionamiento.

Models
=========

- User: Clase que almacena los datos del propietario.
- Car: Clase que almacena los datos del automóvil.
- Parking: Clase que almacena los datos del estacionamiento.

Ejecución
=========

Para la creación del proyecto se utilizó una Base de Datos Postgresql almacenada de manera local, con NAME: 'postgres' y PASSWORD: 'root'.

```sh
python manage.py runserver
```

- La URL index (/) muestra el formulario para almacenar los datos requeridos.
- La URL estacionamiento (/estacionamiento) muestra un formulario el cual solicita el número de patente del vehículo y entrega un response de días, indicando success o failed, éxito o error respectivamente. Si la consulta fue por la patente AB1234, la URL response será /estacionamiento?patente=AB1234.
