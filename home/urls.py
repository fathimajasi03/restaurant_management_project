from django.urls import path
from .views import MenuItemReviewCreateView

urlpatterns = [
    path('menu-items/reviews/', MenuItemReviewCreateView.as_view(), name='menuitem-review-create'),
    ]