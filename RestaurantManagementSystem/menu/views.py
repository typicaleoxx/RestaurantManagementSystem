from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import Menu
from rest_framework.permissions import AllowAny
# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer