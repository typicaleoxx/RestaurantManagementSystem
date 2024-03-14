from django.shortcuts import render
from .models import Waiter
from .serializers import WaiterSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class WaiterViewSet(ModelViewSet):
    queryset=Waiter.objects.all()
    serializer_class=WaiterSerializer
    
