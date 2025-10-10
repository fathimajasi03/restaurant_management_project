from django.urls import path
from .views import UserOrderHistoryAPIView

urlpatterns = [
    path('orders/history/', UserOrderHistoryAPIView.as_view(), name='user-order-history'),
    ]