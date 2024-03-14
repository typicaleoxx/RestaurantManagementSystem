from django.shortcuts import render
from .serializers import TableSerializer
from .models import Table
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class TableViewSet(ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer
