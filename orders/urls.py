from django.urls import path
from .views import OrderSummaryAPIView

urlpatterns = [
    path('orders/<int:pk>/summary/', OrderSummaryAPIView.as_view(), name='order-summary'),
    ]