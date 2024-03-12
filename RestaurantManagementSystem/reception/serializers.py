from rest_framework import serializers
from .models import Reservation
class ReservationSerializer(serializers.Serializer):
    class Meta:
        model=Reservation
        fields="__all__"