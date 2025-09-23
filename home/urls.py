from django.urls import path
from .views import ContactFormSubmissionCreateAPIView

urlpatterns = [
    path('contact/', ContactFormSubmissionCreateAPIView.as_view(), name='contact-form'),
    ]
    