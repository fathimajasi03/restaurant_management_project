from django.urls import path
from .views import RestaurantOpeningHoursAPIView

urlpatterns = [
    path('api/restaurant/opening-hours/', RestaurantOpeningHoursAPIView.as_view())
    ]