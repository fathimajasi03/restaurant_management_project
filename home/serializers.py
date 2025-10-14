from rest_framework import serializers
from .models import UserReview  # Change if your model name differs

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')  # Assuming a foreign key to User model

        class Meta:
                model = UserReview
                        fields = ['user_name', 'rating', 'comment']