# orders/serializers.py
from rest_framework import serializers
from .models import OrderItem

class OrderItemQuantitySerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=0)

        class Meta:
                model = OrderItem
                        fields = ['quantity']

                            def update(self, instance, validated_data):
                                    quantity = validated_data['quantity']
                                            if quantity == 0:
                                                        instance.delete()
                                                                    return instance
                                                                            instance.quantity = quantity
                                                                                    instance.save()
                                                                                            return instance

                                                                                            # orders/views.py
                                                                                            from rest_framework import generics, status
                                                                                            from rest_framework.permissions import IsAuthenticated
                                                                                            from rest_framework.response import Response
                                                                                            from django.shortcuts import get_object_or_404
                                                                                            from .models import OrderItem
                                                                                            from .serializers import OrderItemQuantitySerializer

                                                                                            class UpdateOrderItemQuantityView(generics.UpdateAPIView):
                                                                                                serializer_class = OrderItemQuantitySerializer
                                                                                                    permission_classes = [IsAuthenticated]

                                                                                                        def get_object(self):
                                                                                                                order_item_id = self.kwargs['order_item_id']
                                                                                                                        order_item = get_object_or_404(OrderItem, id=order_item_id)
                                                                                                                                # Ensure user owns the order
                                                                                                                                        if order_item.order.user != self.request.user:
                                                                                                                                                    raise PermissionDenied('Cannot modify items from other orders.')
                                                                                                                                                            return order_item

                                                                                                                                                            # orders/urls.py
                                                                                                                                                            from django.urls import path
                                                                                                                                                            from .views import UpdateOrderItemQuantityView

                                                                                                                                                            urlpatterns = [
                                                                                                                                                                path('api/order-item/<int:order_item_id>/update-quantity/', UpdateOrderItemQuantityView.as_view(), name='update-order-item-quantity'),
                                                                                                                                                                ]