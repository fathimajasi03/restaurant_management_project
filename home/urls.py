from django.urls import path
from .views import MenuItemDetailAPIView
urlpatterns = [
    path('api/menu-items/<int:pk>/', MenuItemDetailAPIView.as_view())
    ]