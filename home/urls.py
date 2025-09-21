from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet

router = DefaultRouter()
router.register('menu-items', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('api/', include(home.urls)),
    ]
    