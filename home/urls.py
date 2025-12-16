# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... existing URLs ...
        path('api/allergens/', views.AllergenListView.as_view(), name='allergen-list'),
        ]