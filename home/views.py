from rest_framework.generics import ListAPIView
from .models import Table
from .serializers import TableSerializer

class TableListAPIView(ListAPIView):
    """
        API endpoint that lists all available tables.
            """
                queryset = Table.objects.filter(is_available=True)
                    serializer_class = TableSerializer