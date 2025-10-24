from rest_framework import serializers
from .models import MenuItem

class FeaturedMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuItem
                    fields = ['id', 'name', 'price', 'description', 'is_featured']  # include fields you want