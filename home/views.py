from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuItemListAPIView(ListAPIView):
    queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer