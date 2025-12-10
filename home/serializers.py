# home/serializers.py
from rest_framework import serializers
from django.db.models import Count
from .models import MenuCategory

class MenuCategoryWithCountSerializer(serializers.ModelSerializer):
    item_count = serializers.IntegerField(read_only=True)

        class Meta:
                model = MenuCategory
                        fields = ['id', 'name', 'item_count']