from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemIngredientListSerializer

class MenuItemIngredientsView(RetrieveAPIView):
    queryset = MenuItem.objects.all()
        serializer_class = MenuItemIngredientListSerializer

            def get(self, request, *args, **kwargs):
                    try:
                                menu_item = self.get_object()
                                        except MenuItem.DoesNotExist:
                                                    return Response({'detail': 'MenuItem not found.'}, status=status.HTTP_404_NOT_FOUND)

                                                            serializer = self.get_serializer(menu_item)
                                                                    return Response(serializer.data)