from order.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['farmer', 'grain_type', 'quantity', 'status']
