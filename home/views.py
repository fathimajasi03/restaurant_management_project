from rest_framework import generics, status
from rest_framework.response import Response
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionCreateAPIView(generics.CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
        serializer_class = ContactFormSubmissionSerializer

            def create(self, request, *args, **kwargs):
                    serializer = self.get_serializer(data=request.data)
                            if serializer.is_valid():
                                        serializer.save()
                                                    return Response(
                                                                    {"success": True, "message": "Contact form submitted successfully."},
                                                                                    status=status.HTTP_201_CREATED
                                                                                                )
                                                                                                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                                                                                        