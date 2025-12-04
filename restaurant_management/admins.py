from django.contrib import admin
from .models import Table  # Add other models as needed

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'is_available']
        list_filter = ['is_available']
            search_fields = ['table_number']