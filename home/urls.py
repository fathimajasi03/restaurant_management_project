from django.urls import path
from .views import AvailableMenuItemsAPIView

urlpatterns = [
    path('menu-items/available/', AvailableMenuItemsAPIView.as_view(), name='available-menu-items'),
    ]