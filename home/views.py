# home/views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import HolidayHours
from .serializers import HolidayHoursSerializer

class HolidayHoursListView(generics.ListAPIView):
    queryset = HolidayHours.objects.all()
        serializer_class = HolidayHoursSerializer
            filter_backends = [DjangoFilterBackend]
                filterset_fields = ['date', 'restaurant']# home/views.py
                from rest_framework import generics
                from django_filters.rest_framework import DjangoFilterBackend
                from .models import HolidayHours
                from .serializers import HolidayHoursSerializer

                class HolidayHoursListView(generics.ListAPIView):
                    queryset = HolidayHours.objects.all()
                        serializer_class = HolidayHoursSerializer
                            filter_backends = [DjangoFilterBackend]
                                filterset_fields = ['date', 'restaurant']