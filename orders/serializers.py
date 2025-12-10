# orders/serializers.py
from rest_framework import serializers
from .models import Reservation

class ReservationStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Reservation.STATUS_CHOICES)

        class Meta:
                model = Reservation
                        fields = ['status']