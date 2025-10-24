# home/admin.py

from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email')
        search_fields = ('name', 'address')
            list_filter = ('is_active',)  # Add only if Restaurant model has 'is_active' BooleanField

            admin.site.register(Restaurant, RestaurantAdmin)