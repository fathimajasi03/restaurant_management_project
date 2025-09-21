# models.py (example)
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        description = models.TextField(blank=True)
            price = models.DecimalField(max_digits=6, decimal_places=2)
                available = models.BooleanField(default=True)

                # serializers.py
                from rest_framework import serializers
                from .models import MenuItem

                class MenuItemSerializer(serializers.ModelSerializer):
                    class Meta:
                            model = MenuItem
                                    fields = ['id', 'name', 'description', 'price', 'available']

                                        # Validate price to be positive
                                            def validate_price(self, value):
                                                    if value < 0:
                                                                raise serializers.ValidationError("Price must be a positive number.")
                                                                        return value
