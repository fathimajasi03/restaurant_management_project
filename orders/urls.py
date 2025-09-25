from django.urls import path
from .views import UpdateOrderStatusAPIView

urlpatterns = [
    path('orders/<int:pk>/update-status/', UpdateOrderStatusAPIView.as_view(), name='update-order-status'),
    ]
    