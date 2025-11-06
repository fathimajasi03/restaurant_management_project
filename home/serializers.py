from rest_framework import serializers
from .models import Restaurant, DailyOperatingHours

class RestaurantSerializer(serializers.ModelSerializer):
    daily_operating_hours = DailyOperatingHoursSerializer(many=True, read_only=True)

        class Meta:
                model = Restaurant
                        fields = ['id', 'name', 'address', 'phone', 'daily_operating_hours']