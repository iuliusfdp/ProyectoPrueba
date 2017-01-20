from django.test import TestCase
from parking.models import User
from parking.forms import OwnerForm
# models test


class ParkingTest(TestCase):

    def create_user(self, rut="175115250", nombre="Julian", apellido="Delgado", sexo="H", edad=27):
        return User.objects.create(rut=rut, nombre=nombre, apellido=apellido, sexo=sexo, edad=edad)

    def test_user_creation(self):
        w = self.create_user()
        self.assertTrue(isinstance(w, User))

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_data(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        resp = self.client.post(
            '/', {'RUT': '195563039', 'nombre': 'paola', 'apellido': 'delgado', 'sexo': 'M', 'edad': 19,
                  'patente': 'ASDS21', 'marca': 'chevrolet', 'color': 'Rojo', 'chasis': 'as',
                  'numero': 111, 'dias': 7})
        self.assertEqual(resp.status_code, 200)

    def test_index_invalid_rut(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        resp = self.client.post(
            '/', {'RUT': '195563038', 'nombre': 'paola', 'apellido': 'delgado', 'sexo': 'M', 'edad': 19,
                  'patente': 'ASDS21', 'marca': 'chevrolet', 'color': 'Rojo', 'chasis': 'as',
                  'numero': 111, 'dias': 7})
        self.assertEqual(resp.status_code, 200)

    def test_parking_empty_data(self):
        response = self.client.get('/estacionamiento', {'patente': ''})
        self.assertEqual(response.status_code, 200)

    def test_parking_correct_data(self):
        response = self.client.get('/estacionamiento', {'patente': '231m'})
        self.assertEqual(response.status_code, 200)

    def test_forms(self):
        form_data = {'RUT': '195563039', 'nombre': 'paola',
                     'apellido': 'delgado', 'sexo': 'M', 'edad': 19}
        form = OwnerForm(data=form_data)
        self.assertTrue(form.is_valid())
