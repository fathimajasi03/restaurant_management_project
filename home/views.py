from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSearchSerializer
class MenuItemSearchAPIView(ListAPIView):
    serializer_class = MenuItemSearchSerializer
        def get_queryset(self):
                query = self.request.GET.get('q')
                        if query:
                                    return MenuItem.objects.filter(name__icontains=query)
                                            return MenuItem.objects.none()