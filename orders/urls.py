from django.urls import path
from .views import UserOrderHistoryAPIView

urlpatterns = [
    path('order-history/', UserOrderHistoryAPIView.as_view(), name='order-history'),
    ]
