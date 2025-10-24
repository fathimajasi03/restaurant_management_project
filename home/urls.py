from django.urls import path
from .views import FeaturedMenuItemsListView

urlpatterns = [
    path('api/menu-items/featured/', FeaturedMenuItemsListView.as_view(), name='featured-menu-items'),
    ]