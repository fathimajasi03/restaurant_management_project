# home/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

# Define urlpatterns including router URLs
urlpatterns = [
    path('api/', include(router.urls)),
    ]
    