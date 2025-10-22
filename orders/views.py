from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
        serializer_class = TableSerializer