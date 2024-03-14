from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Reservation, Bill
from .serializers import BillSerializer, ReservationSerializer
# Create your views here.
class ReservationViewSet(ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
class BillViewSet(ModelViewSet):
    queryset=Bill.objects.all()
    serializer_class=BillSerializer
