# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/reservation/<int:reservation_id>/status/', 
             views.UpdateReservationStatusView.as_view(), 
                      name='update-reservation-status'),
                      ]