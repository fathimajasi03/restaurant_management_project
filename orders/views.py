from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order

class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

        def delete(self, request, order_id):
                try:
                            order = Order.objects.get(id=order_id)
                                    except Order.DoesNotExist:
                                                return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

                                                        if order.user != request.user:
                                                                    return Response({"error": "You are not authorized to cancel this order."},
                                                                                                status=status.HTTP_403_FORBIDDEN)

                                                                                                        if order.status == 'Cancelled':
                                                                                                                    return Response({"message": "Order is already cancelled."}, status=status.HTTP_400_BAD_REQUEST)

                                                                                                                            order.status = 'Cancelled'
                                                                                                                                    order.save()
                                                                                                                                            return Response({"message": "Order cancelled successfully."}, status=status.HTTP_200_OK)
                                                                                                                                            