from rest_framework import serializers
from .models import Waiter

class WaiterSerializer(serializers.Serializer):
    class Meta:
        model=Waiter
        fields= "__all__"