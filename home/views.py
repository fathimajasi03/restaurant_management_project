from rest_framework import generics
from .models import Cuisine
from .serializers import CuisineSerializer

class CuisineListView(generics.ListAPIView):
    queryset = Cuisine.objects.all()
        serializer_class = CuisineSerializer