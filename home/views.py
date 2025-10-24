from rest_framework import generics
from .models import MenuItem
from .serializers import FeaturedMenuItemSerializer

class FeaturedMenuItemsListView(generics.ListAPIView):
    serializer_class = FeaturedMenuItemSerializer

        def get_queryset(self):
                return MenuItem.objects.filter(is_featured=True)