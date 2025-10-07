from django.urls import path
from .views import MenuItemPriceRangeAPIView

urlpatterns = [
    path('api/menu-items/price-range/', MenuItemPriceRangeAPIView.as_view())
    ]