# home/serializers.py
from rest_framework import serializers
from .models import HolidayHours

class HolidayHoursSerializer(serializers.ModelSerializer):
    class Meta:
            model = HolidayHours
                    fields = ['id', 'restaurant', 'date', 'opening_time', 'closing_time', 'description']