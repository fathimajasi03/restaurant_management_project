from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
                    fields = ['username', 'first_name', 'last_name', 'email']
                            read_only_fields = ['username']
                            