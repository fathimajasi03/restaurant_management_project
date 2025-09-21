from django.urls import path
from .views import MenuItemByCategoryView

urlpatterns = [
    # other URL patterns...
        path('menu-items-by-category/', MenuItemByCategoryView.as_view(), name='menu-items-by-category'),
        ]
        