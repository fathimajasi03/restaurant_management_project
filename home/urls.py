from django.urls import path
from .views import TableListAPIView

urlpatterns = [
    path('api/tables/', TableListAPIView.as_view(), name='table-list'),
    ]