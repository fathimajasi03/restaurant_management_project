from django.urls import path
from .views import CuisineListView

urlpatterns = [
    path('api/cuisines/', CuisineListView.as_view(), name='cuisine-list'),
    ]