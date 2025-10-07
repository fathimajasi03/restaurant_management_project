from django.urls import path
from .views import MenuItemListAPIView
urlpatterns = [
    path('api/menu-items/',MenuItemListAPIView.as_view())
    ]