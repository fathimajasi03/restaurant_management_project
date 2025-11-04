from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET', 'POST'])
def menuitem_list_create(request):
    restaurant_id = request.query_params.get('restaurant_id')
        if request.method == 'GET':
                queryset = MenuItem.objects.all()
                        if restaurant_id:
                                    queryset = queryset.filter(restaurant__id=restaurant_id)
                                            serializer = MenuItemSerializer(queryset, many=True)
                                                    return Response(serializer.data)
                                                        elif request.method == 'POST':
                                                                serializer = MenuItemSerializer(data=request.data)
                                                                        if serializer.is_valid():
                                                                                    serializer.save()
                                                                                                return Response(serializer.data, status=status.HTTP_201_CREATED)
                                                                                                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                                                                                        @api_view(['GET', 'PUT', 'DELETE'])
                                                                                                        def menuitem_detail(request, pk):
                                                                                                            try:
                                                                                                                    item = MenuItem.objects.get(pk=pk)
                                                                                                                        except MenuItem.DoesNotExist:
                                                                                                                                return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

                                                                                                                                    if request.method == 'GET':
                                                                                                                                            serializer = MenuItemSerializer(item)
                                                                                                                                                    return Response(serializer.data)

                                                                                                                                                        elif request.method == 'PUT':
                                                                                                                                                                serializer = MenuItemSerializer(item, data=request.data)
                                                                                                                                                                        if serializer.is_valid():
                                                                                                                                                                                    serializer.save()
                                                                                                                                                                                                return Response(serializer.data)
                                                                                                                                                                                                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                                                                                                                                                                                            elif request.method == 'DELETE':
                                                                                                                                                                                                                    item.delete()
                                                                                                                                                                                                                            return Response(status=status.HTTP_204_NO_CONTENT)