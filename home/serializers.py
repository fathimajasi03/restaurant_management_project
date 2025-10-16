from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
            model = Table
                    fields = '__all__'  # Include all fields (table_number, capacity, is_available, etc.)