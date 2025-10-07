from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemPriceRangeAPIView(ListAPIView):
    serializer_class = MenuItemSerializer

        def get_queryset(self):
                queryset = MenuItem.objects.all()
                        min_price = self.request.query_params.get('min_price')
                                max_price = self.request.query_params.get('max_price')
                                        try:
                                                    if min_price is not None:
                                                                    min_price = float(min_price)
                                                                                    queryset = queryset.filter(price__gte=min_price)
                                                                                                if max_price is not None:
                                                                                                                max_price = float(max_price)
                                                                                                                                queryset = queryset.filter(price__lte=max_price)
                                                                                                                                        except ValueError:
                                                                                                                                                    return MenuItem.objects.none()
                                                                                                                                                            return queryset

                                                                                                                                                                def list(self, request, *args, **kwargs):
                                                                                                                                                                        queryset = self.get_queryset()
                                                                                                                                                                                if queryset is None:
                                                                                                                                                                                            return Response({"error": "Invalid price parameters"}, status=status.HTTP_400_BAD_REQUEST)
                                                                                                                                                                                                    serializer = self.get_serializer(queryset, many=True)
                                                                                                                                                                                                            return Response(serializer.data)