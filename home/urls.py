from django.urls import path
from .views import UserReviewCreateView, MenuItemReviewsListView

urlpatterns = [
    path('reviews/', UserReviewCreateView.as_view(), name='review-create'),
        path('menu-items/<int:menu_item_id>/reviews/', MenuItemReviewsListView.as_view(), name='menuitem-reviews'),
        ]
        