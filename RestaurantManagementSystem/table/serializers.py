from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.Serializer):
    class Meta:
        model=Table
        fields="__all__"
