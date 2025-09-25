from django.urls import path
from .views import DailySpecialsListAPIView

urlpatterns = [
    # other urls
        path('daily-specials/', DailySpecialsListAPIView.as_view(), name='daily-specials'),
        ]
        