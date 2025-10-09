from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer

class AvailableMenuItemsAPIView(ListAPIView):
    serializer_class = MenuItemSerializer

        def get_queryset(self):
                return MenuItem.objects.filter(available=True)