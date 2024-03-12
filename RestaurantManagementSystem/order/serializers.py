from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = "__all__"
