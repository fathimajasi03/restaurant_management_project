   from rest_framework import generics, status, permissions
   from rest_framework.response import Response
   from .models import Order
   from .serializers import OrderStatusUpdateSerializer
   
   class UpdateOrderStatusAPIView(generics.UpdateAPIView):
       queryset = Order.objects.all()
           serializer_class = OrderStatusUpdateSerializer
               permission_classes = [permissions.IsAuthenticated]
               
                   def put(self, request, pk):
                           try:
                                       order = Order.objects.get(pk=pk)
                                               except Order.DoesNotExist:
                                                           return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
                                                           
                                                                   if order.user != request.user:
                                                                               return Response({"error": "You are not authorized to update this order."}, status=status.HTTP_403_FORBIDDEN)
                                                                               
                                                                                       serializer = self.get_serializer(order, data=request.data)
                                                                                               if serializer.is_valid():
                                                                                                           serializer.save()
                                                                                                                       return Response({"success": "Order status updated successfully."}, status=status.HTTP_200_OK)
                                                                                                                               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                                                                   return Res                                                                                                                                       