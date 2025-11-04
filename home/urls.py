from django.urls import path
from .views import menuitem_list_create, menuitem_detail

urlpatterns = [
    path('menu-items/', menuitem_list_create, name='menuitem-list-create'),
        path('menu-items/<int:pk>/', menuitem_detail, name='menuitem-detail'),
        ]