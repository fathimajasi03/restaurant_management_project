from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem

class AvailableMenuItemCountAPIView(APIView):
    def get(self, request, *args, **kwargs):
            try:
                        total_available = MenuItem.objects.filter(is_available=True).count()
                                    return Response({"total_menu_items": total_available}, status=status.HTTP_200_OK)
                                            except Exception:
                                                        # Optional: log the exception here
                                                                    return Response(
                                                                                    {"error": "Could not retrieve menu item count."},
                                                                                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                )