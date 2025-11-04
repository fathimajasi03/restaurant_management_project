from django.contrib import admin
from .models import Order

def mark_orders_processed(modeladmin, request, queryset):
    """
        Admin action to mark selected orders as 'Processed'.
            """
                updated = queryset.update(status='Processed')
                    modeladmin.message_user(request, f"{updated} orders marked as Processed.")

                    mark_orders_processed.short_description = "Mark selected orders as Processed"

                    @admin.register(Order)
                    class OrderAdmin(admin.ModelAdmin):
                        list_display = ['id', 'status', 'created_at']  # add/adjust fields as needed
                            actions = [mark_orders_processed]