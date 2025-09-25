       from rest_framework import serializers
       from .models import Order

       class OrderStatusUpdateSerializer(serializers.ModelSerializer):
           class Meta:
                   model = Order
                           fields = ['status']

                               def validate_status(self, value):
                                       allowed_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
                                               if value not in allowed_statuses:
                                                           raise serializers.ValidationError("Invalid status.")
                                                                   return value
                                                                                                    