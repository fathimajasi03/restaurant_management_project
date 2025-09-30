from rest_framework.generics import RetrieveAPIView
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantDetailAPIView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
        serializer_class = RestaurantSerializer
        