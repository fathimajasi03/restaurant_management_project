from rest_framework import serializers
from .models import Order, OrderItem
from home.serializers import MenuItemSerializer  # assuming you have this

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.StringRelatedField()

        class Meta:
                model = OrderItem
                        fields = ['menu_item', 'quantity', 'price']

                        class OrderSerializer(serializers.ModelSerializer):
                            items = OrderItemSerializer(many=True, read_only=True)

                                class Meta:
                                        model = Order
                                                fields = ['id', 'order_date', 'total_price', 'items']
                                                