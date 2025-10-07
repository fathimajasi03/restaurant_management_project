from rest_framework.generics import RetrieveAPIView
from .models import MenuItem
from .serializers import MenuItemDetailSerializer
class MenuItemDetailAPIView(RetrieveAPIView):
    queryset = MenuItem.objects.all()
        serializer_class = MenuItemDetailSerializer