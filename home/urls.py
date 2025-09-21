# home/urls.py

from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet
from django.urls import path, include

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet, basename='menuitem')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),  # Include all router-registered URLs under 'api/'
    ]
    