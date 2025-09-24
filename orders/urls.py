from django.urls import path
from .views import CancelOrderView

urlpatterns = [
    # Other url patterns ...
        path('orders/<int:order_id>/cancel/', CancelOrderView.as_view(), name='cancel-order'),
        ]
        