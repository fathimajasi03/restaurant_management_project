from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Order
from .serializers import OrderHistorySerializer

class OrderHistoryPagination(PageNumberPagination):
    page_size = 10
        page_size_query_param = 'page_size'
            max_page_size = 50

            class UserOrderHistoryAPIView(ListAPIView):
                serializer_class = OrderHistorySerializer
                    permission_classes = [IsAuthenticated]
                        pagination_class = OrderHistoryPagination

                            def get_queryset(self):
                                    return Order.objects.filter(user=self.request.user).order_by('-created_at')