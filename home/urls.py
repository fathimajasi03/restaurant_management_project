# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/holiday-hours/', views.HolidayHoursListView.as_view(), name='holiday-hours-list'),
    ]