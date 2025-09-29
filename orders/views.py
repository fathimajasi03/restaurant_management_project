from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order

@api_view(['GET'])
def order_status(request, order_id):
    try:
            order = Order.objects.get(pk=order_id)
                except Order.DoesNotExist:
                        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
                            return Response({'order_id': order.id, 'status': order.status}, status=status.HTTP_200_OK)
                            