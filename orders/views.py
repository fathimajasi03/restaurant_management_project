from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderStatusSerializer
class OrderStatusAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderStatusSerializer
            lookup_field = 'unique_id'