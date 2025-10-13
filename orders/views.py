from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated  # Optional: add if you want auth
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderStatusUpdateSerializer

class OrderStatusUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderStatusUpdateSerializer
            lookup_field = 'pk'  # Order ID in URL

                def put(self, request, *args, **kwargs):
                        """
                                Override to add custom error handling or behavior if needed.
                                        """
                                                return self.update(request, *args, **kwargs)

                                                    def patch(self, request, *args, **kwargs):
                                                            """
                                                                    Allow partial update with PATCH.
                                                                            """
                                                                                    return self.partial_update(request, *args, **kwargs)