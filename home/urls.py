from django.urls import path
from .views import RestaurantDetailAPIView

urlpatterns = [
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
    ]
    