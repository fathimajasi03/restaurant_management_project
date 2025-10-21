from rest_framework import serializers
from .models import UserReviews

class UserReviewsSerializer(serializers.ModelSerializer):
    class Meta:
            model = UserReviews
                    fields = ['id', 'user', 'menu_item', 'rating', 'comment', 'created_at']
                            read_only_fields = ['user', 'created_at']