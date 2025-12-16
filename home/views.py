# home/views.py
from rest_framework import generics
from .models import Allergen
from .serializers import AllergenSerializer

class AllergenListView(generics.ListAPIView):
    queryset = Allergen.objects.all()
        serializer_class = AllergenSerializer