# home/views.py
from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategoryWithCountSerializer

class MenuCategoriesView(generics.ListAPIView):
    serializer_class = MenuCategoryWithCountSerializer

        def get_queryset(self):
                return MenuCategory.objects.annotate(
                            item_count=Count('menuitem')
                                    )