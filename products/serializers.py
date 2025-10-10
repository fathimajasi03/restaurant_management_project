from rest_framework import serializers
from .models import Order

class OrderHistorySerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)  # Or use a nested serializer for more detail

        class Meta:
                model = Order
                        fields = ['id', 'created_at', 'items', 'total_amount', 'status']