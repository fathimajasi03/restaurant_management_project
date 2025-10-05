from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
        serializer_class = MenuCategorySerializer