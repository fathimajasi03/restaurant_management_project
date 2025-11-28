# home/admin.py
from django.contrib import admin
from .models import DailySpecial

@admin.register(DailySpecial)
class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'date')