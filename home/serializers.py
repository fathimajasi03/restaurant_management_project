from rest_framework import serializers
from .models import UserReview

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
            model = UserReview
                    fields = ['id', 'menu_item', 'user', 'rating', 'comment', 'created_at']
                            read_only_fields = ['id', 'created_at', 'user']

                                def validate_rating(self, value):
                                        if value < 1 or value > 5:
                                                    raise serializers.ValidationError('Rating must be between 1 and 5.')
                                                            return value
                                                            