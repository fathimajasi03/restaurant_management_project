from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem

class MenuItemAvailabilityAPIView(APIView):
    def get(self, request, pk):
            try:
                        menu_item = MenuItem.objects.get(pk=pk)
                                except MenuItem.DoesNotExist:
                                            return Response({'error': 'Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)

                                                    return Response({'available': menu_item.is_available})