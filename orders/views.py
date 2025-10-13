from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSummarySerializer

class OrderSummaryAPIView(APIView):
    def get(self, request, pk):
            try:
                        order = Order.objects.get(pk=pk)
                                except Order.DoesNotExist:
                                            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

                                                    serializer = OrderSummarySerializer(order)
                                                            return Response(serializer.data)