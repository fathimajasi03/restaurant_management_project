from django.urls import path
from .views import MenuCategoryListView

"""
URL patterns for the home app including the menu categories API endpoint.
"""

urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
    ]
    