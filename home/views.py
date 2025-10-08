from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import UserReview
from .serializers import ReviewSerializer

class ReviewPagination(PageNumberPagination):
    page_size = 10
        page_size_query_param = 'page_size'
            max_page_size = 50

            class ReviewListAPIView(ListAPIView):
                queryset = UserReview.objects.all().order_by('-created_at')  # Order newest first
                    serializer_class = ReviewSerializer
                        pagination_class = ReviewPagination

                            def list(self, request, *args, **kwargs):
                                    try:
                                                return super().list(request, *args, **kwargs)
                                                        except Exception as e:
                                                                    return Response({'error': 'An error occurred while fetching reviews.'},
                                                                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)