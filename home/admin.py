from django.contrib import admin
from .models import MenuItem

def make_unavailable(modeladmin, request, queryset):
    for item in queryset:
            item.is_available = False
                    item.save()
                    make_unavailable.short_description = "Mark selected menu items as unavailable"

                    @admin.register(MenuItem)
                    class MenuItemAdmin(admin.ModelAdmin):
                        list_display = ['name', 'is_available', 'price']  # adjust fields as needed
                            actions = [make_unavailable]