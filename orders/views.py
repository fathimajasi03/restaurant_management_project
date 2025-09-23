from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from orders.utils import generate_unique_order_id

# Example usage during order creation
unique_id = generate_unique_order_id()
order = Order.objects.create(order_id=unique_id, ...)  # add other fields as needed


class UserOrderHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

        def get(self, request):
                user = request.user
                        orders = Order.objects.filter(user=user).order_by('-order_date')
                                serializer = OrderSerializer(orders, many=True)
                                        return Response(serializer.data)
                                        