# home/admin.py
from django.contrib import admin
from .models import MenuItem, Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    @admin.register(MenuItem)
    class MenuItemAdmin(admin.ModelAdmin):
        list_display = ('name', 'price', 'is_available')
            filter_horizontal = ('ingredients',)