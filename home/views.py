from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
        serializer_class = ReviewSerializer
            permission_classes = [IsAuthenticated]

                def perform_create(self, serializer):
                        serializer.save(user=self.request.user)