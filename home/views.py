from rest_framework import viewsets
from .models import MenuCategory
from rest_framework import serializers

# Serializer (inline or in serializers.py)
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuCategory
                    fields = ['id', 'name']

                    # ViewSet for listing categories
                    class MenuCategoryViewSet(viewsets.ReadOnlyModelViewSet):
                        queryset = MenuCategory.objects.all()
                            serializer_class = MenuCategorySerializer