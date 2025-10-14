from rest_framework.generics import ListAPIView
from .models import UserReview
from .serializers import ReviewSerializer

class ReviewListAPIView(ListAPIView):
    queryset = UserReview.objects.all().order_by('-created_at')  # Optional ordering newest first
        serializer_class = ReviewSerializer