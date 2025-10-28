from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    ]0