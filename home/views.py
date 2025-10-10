from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQPagination(PageNumberPagination):
    page_size = 10
        page_size_query_param = 'page_size'
            max_page_size = 50

            class FAQListAPIView(ListAPIView):
                queryset = FAQ.objects.all().order_by('id')
                    serializer_class = FAQSerializer
                        pagination_class = FAQPagination

                            def list(self, request, *args, **kwargs):
                                    try:
                                                return super().list(request, *args, **kwargs)
                                                        except Exception:
                                                                    return Response(
                                                                                    {"error": "An error occurred while retrieving FAQs."},
                                                                                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                                                                                                )