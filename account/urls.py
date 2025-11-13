from django.urls import path
from .views import MyLoyaltyPointsView

urlpatterns = [
    path('api/my-loyalty-points/', MyLoyaltyPointsView.as_view(), name='my-loyalty-points'),
    ]