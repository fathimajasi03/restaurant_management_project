from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemAvailabilitySerializer

@api_view(['PATCH'])
def update_menu_item_availability(request, pk):
    try:
            menu_item = MenuItem.objects.get(pk=pk)
                except MenuItem.DoesNotExist:
                        return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

                            serializer = MenuItemAvailabilitySerializer(menu_item, data=request.data, partial=True)
                                if serializer.is_valid():
                                        serializer.save()
                                                return Response({"message": "Availability updated successfully.", "data": serializer.data})
                                                    else:
                                                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)