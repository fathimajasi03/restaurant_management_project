from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Order

class UpdateOrderStatusAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
        def post(self, request):
                order_id = request.data.get('order_id')
                        new_status = request.data.get('status')
                        
                                # Validate status
                                        allowed_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
                                                if new_status not in allowed_statuses:
                                                            return Response({'error': 'Invalid status.'},
                                                                                        status=status.HTTP_400_BAD_REQUEST)
                                                                                        
                                                                                                # Validate order
                                                                                                        try:
                                                                                                                    order = Order.objects.get(id=order_id)
                                                                                                                            except Order.DoesNotExist:
                                                                                                                                        return Response({'error': 'Invalid order ID.'},
                                                                                                                                                                    status=status.HTTP_404_NOT_FOUND)
                                                                                                                                                                    
                                                                                                                                                                            # Optional: Ensure only owner can update
                                                                                                                                                                                    if order.user != request.user:
                                                                                                                                                                                                return Response({'error': 'Not authorized.'},
                                                                                                                                                                                                                            status=status.HTTP_403_FORBIDDEN)
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                    # Update status
                                                                                                                                                                                                                                            order.status = new_status
                                                                                                                                                                                                                                                    order.save()
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                            return Response({'message': f'Order status updated to {new_status}.'},
                                                                                                                                                                                                                                                                                    status=status.HTTP_200_OK)
                                                                                                                                                                                                                                                                                                                                                                                                                                                              return Res                                                                                                                                       