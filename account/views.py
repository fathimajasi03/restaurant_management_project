from rest_framework import viewsets
from account.models import Staff
from account.serializers import StaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
        serializer_class = StaffSerializer