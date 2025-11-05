from django.urls import path
from .views import PaymentMethodListAPIView

urlpatterns = [
    path('api/payment-methods/', PaymentMethodListAPIView.as_view(), name='payment-methods-list'),
    ]