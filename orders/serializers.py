from rest_framework import serializers
from .models import Order, OrderItem  # Adjust import if your order item model name differs

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
            model = OrderItem
                    fields = ['id', 'menu_item_name', 'quantity', 'price']  # Adjust fields as per your model

                    class OrderSummarySerializer(serializers.ModelSerializer):
                        items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')  # Adjust source if related_name set
                            total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

                                class Meta:
                                        model = Order
                                                fields = ['id', 'total_price', 'status', 'items']