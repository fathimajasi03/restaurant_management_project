from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPagination(PageNumberPagination):
    page_size = 10  # You can set this as needed

    class MenuItemViewSet(ReadOnlyModelViewSet):
        queryset = MenuItem.objects.all()
            serializer_class = MenuItemSerializer
                pagination_class = MenuItemPagination
                    filter_backends = [SearchFilter]
                        search_fields = ['name']
                        