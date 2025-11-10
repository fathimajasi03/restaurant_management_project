from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'is_active')  # Add 'is_active' to the displayed columns
        list_editable = ('is_active',)  # Make 'is_active' editable directly from the list view

        admin.site.register(Coupon, CouponAdmin)