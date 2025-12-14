# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... existing URLs ...
        path('api/shifts/', views.StaffShiftListView.as_view(), name='staff-shifts'),
        ]