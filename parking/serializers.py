from parking.models import User, Car, Parking
from rest_framework import serializers


class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('numero', 'dias')