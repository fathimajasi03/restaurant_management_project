from django.urls import path
from .views import ReviewListAPIView
urlpatterns = [
    path('api/reviews/', ReviewListAPIView.as_view())
    ]