from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuCategory
                    fields = ['id', 'name']
                            read_only_fields = ['id']
                            