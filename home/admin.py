class MenuItemAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_available', 'is_gluten_free']  # add other fields as needed