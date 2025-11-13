from rest_framework import serializers

class UserLoyaltySerializer(serializers.Serializer):
    loyalty_points = serializers.IntegerField()