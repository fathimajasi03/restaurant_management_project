from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant

class RestaurantOpeningHoursAPIView(APIView):
    def get(self, request):
            restaurant = Restaurant.objects.first()
                    opening_hours = restaurant.opening_hours if restaurant else "Not available"
                            return Response({"opening_hours": opening_hours})