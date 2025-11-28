# home/models.py
from django.db import models

class Staff(models.Model):
    CHEF = 'Chef'
        WAITER = 'Waiter'
            MANAGER = 'Manager'

                ROLE_CHOICES = [
                        (CHEF, 'Chef'),
                                (WAITER, 'Waiter'),
                                        (MANAGER, 'Manager'),
                                            ]

                                                first_name = models.CharField(max_length=100)
                                                    last_name = models.CharField(max_length=100)
                                                        role = models.CharField(max_length=10, choices=ROLE_CHOICES)
                                                            contact_email = models.EmailField()

                                                                def __str__(self):
                                                                        return f"{self.first_name} {self.last_name} - {self.role}"

                                                                        # home/admin.py
                                                                        from django.contrib import admin
                                                                        from .models import Staff

                                                                        @admin.register(Staff)
                                                                        class StaffAdmin(admin.ModelAdmin):
                                                                            list_display = ('first_name', 'last_name', 'role', 'contact_email')
                                                                                list_filter = ('role',)
                                                                                    search_fields = ('first_name', 'last_name', 'contact_email')