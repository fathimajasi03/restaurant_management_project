from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, UserReviews
from .serializers import UserReviewsSerializer

class MenuItemReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

        def post(self, request, *args, **kwargs):
                menu_item_id = request.data.get('menu_item_id')
                        rating = request.data.get('rating')
                                comment = request.data.get('comment', '')

                                        # Validate existence of the menu item
                                                try:
                                                            menu_item = MenuItem.objects.get(pk=menu_item_id)
                                                                    except MenuItem.DoesNotExist:
                                                                                return Response({'error': 'Menu item not found.'}, status=status.HTTP_404_NOT_FOUND)
                                                                                        
                                                                                                # Validate rating
                                                                                                        if not isinstance(rating, int) or rating < 1 or rating > 5:
                                                                                                                    return Response({'error': 'Rating must be an integer between 1 and 5.'}, status=status.HTTP_400_BAD_REQUEST)

                                                                                                                            review = UserReviews.objects.create(
                                                                                                                                        user=request.user,
                                                                                                                                                    menu_item=menu_item,
                                                                                                                                                                rating=rating,
                                                                                                                                                                            comment=comment
                                                                                                                                                                                    )
                                                                                                                                                                                            serializer = UserReviewsSerializer(review)
                                                                                                                                                                                                    return Response(serializer.data, status=status.HTTP_201_CREATED)