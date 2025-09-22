from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

        def retrieve(self, request):
                serializer = UserProfileSerializer(request.user)
                        return Response(serializer.data)

                            def update(self, request):
                                    serializer = UserProfileSerializer(request.user, data=request.data)
                                            serializer.is_valid(raise_exception=True)
                                                    serializer.save()
                                                            return Response(serializer.data)
                                                            