from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemByCategoryView(APIView):
    def get(self, request):
            category_name = request.query_params.get('category', None)

                    if not category_name:
                                return Response({"error": "Category parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

                                        items = MenuItem.objects.filter(category__category_name=category_name)
                                                serializer = MenuItemSerializer(items, many=True)
                                                        return Response(serializer.data)
                                                        