from django.urls import path
from .views import UserProfileViewSet

user_profile = UserProfileViewSet.as_view({
    'get': 'retrieve',
        'put': 'update',
        })

        urlpatterns = [
            path('profile/', user_profile, name='user-profile'),
            ]
            