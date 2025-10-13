from django.urls import path
from .views import AvailableMenuItemCountAPIView

urlpatterns = [
    path('menu-items/available/count/', AvailableMenuItemCountAPIView.as_view(), name='available-menu-items-count'),
    ]