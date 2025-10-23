from rest_framework.generics import ListAPIView
from .models import Cuisine
from .serializers import CuisineSerializer

class CuisineListView(ListAPIView):
    queryset = Cuisine.objects.all()
        serializer_class = CuisineSerializer