from rest_framework import viewsets
from rest_framework import filters
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer
            filter_backends = [filters.SearchFilter]
                search_fields = ['category']  # Enables ?search=CategoryName

                    def get_queryset(self):
                            queryset = super().get_queryset()
                                    category = self.request.query_params.get('category')
                                            if category:
                                                        queryset = queryset.filter(category=category)
                                                                return queryset