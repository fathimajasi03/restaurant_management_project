 from rest_framework import generics
 from .models import MenuItem
 from .serializers import DailySpecialSerializer

 class DailySpecialsListAPIView(generics.ListAPIView):
     queryset = MenuItem.objects.filter(is_daily_special=True)
         serializer_class = DailySpecialSerializer
                                           