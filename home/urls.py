# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... existing paths ...
        path('api/menu/active/', views.ActiveMenuItemsView.as_view(), name='active-menu-items'),
        ]