from django.urls import path
from .views import MenuItemAvailabilityAPIView

urlpatterns = [
    path('menu-items/<int:pk>/availability/', MenuItemAvailabilityAPIView.as_view(), name='menuitem-availability'),
    ]