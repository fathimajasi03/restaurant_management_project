from django.urls import path
from .views import order_status

urlpatterns = [
    path('orders/<int:order_id>/status/', order_status, name='order-status'),
    ]
    