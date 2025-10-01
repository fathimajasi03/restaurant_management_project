from django.urls import path
from .views import update_menu_item_availability

urlpatterns = [
    path('menu-items/<int:pk>/availability/', update_menu_item_availability, name='update-menuitem-availability'),
    ]