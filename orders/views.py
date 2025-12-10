# orders/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Reservation
from .serializers import ReservationStatusSerializer

class UpdateReservationStatusView(generics.UpdateAPIView):
    serializer_class = ReservationStatusSerializer
        permission_classes = [IsAuthenticated]

            def get_object(self):
                    return get_object_or_404(Reservation, id=self.kwargs['reservation_id'])