from rest_framework import serializers
from .models import MenuItem, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
            model = Ingredient
                    fields = ['id', 'name']  # Include relevant Ingredient fields

                    class MenuItemIngredientListSerializer(serializers.ModelSerializer):
                        ingredients = IngredientSerializer(many=True, read_only=True)

                            class Meta:
                                    model = MenuItem
                                            fields = ['id', 'name', 'ingredients']  # Include MenuItem fields you want plus ingredients