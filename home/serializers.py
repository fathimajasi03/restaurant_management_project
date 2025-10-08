from rest_framework import serializers
from .models import UserReview  # Adjust if your review model name differs

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
            model = UserReview
                    fields = ['id', 'comment', 'rating']