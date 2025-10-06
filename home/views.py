from rest_framework.generics import ListAPIView
from .models import OpeningHours
from .serializers import OpeningHoursSerializer

class OpeningHoursListAPIView(ListAPIView):
    queryset = OpeningHours.objects.all().order_by('id')
        serializer_class = OpeningHoursSerializer