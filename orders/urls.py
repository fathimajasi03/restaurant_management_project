from django.urls import path
from .views import OrderStatusUpdateAPIView

urlpatterns = [
    path('orders/<int:pk>/status/', OrderStatusUpdateAPIView.as_view(), name='order-status-update'),
    ]