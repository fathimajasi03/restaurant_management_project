from django.urls import path
from .views import FeedbackListAPIView

urlpatterns = [
    path('api/feedback/', FeedbackListAPIView.as_view(), name='feedback-list'),
    ]