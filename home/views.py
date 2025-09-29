from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserReview
from .serializers import UserReviewSerializer

class UserReviewCreateView(CreateAPIView):
    serializer_class = UserReviewSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

            def perform_create(self, serializer):
                    serializer.save(user=self.request.user)

                    class MenuItemReviewsListView(ListAPIView):
                        serializer_class = UserReviewSerializer

                            def get_queryset(self):
                                    menu_item_id = self.kwargs['menu_item_id']
                                            return UserReview.objects.filter(menu_item_id=menu_item_id)
                                            