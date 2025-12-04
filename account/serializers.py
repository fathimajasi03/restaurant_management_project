from rest_framework import serializers
from account.models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
            model = Staff
                    fields = '__all__'