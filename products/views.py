from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderSerializer
            permission_classes = [IsAuthenticated]
                lookup_field = 'id'
                