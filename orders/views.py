from rest_framework.generics import ListAPIView
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

class PaymentMethodListAPIView(ListAPIView):
    serializer_class = PaymentMethodSerializer

        def get_queryset(self):
                # Only return active payment methods
                        return PaymentMethod.objects.filter(is_active=True)