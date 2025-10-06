from django.db import models

class Restaurant(models.Model):
    # existing fields ...

        def get_total_menu_items(self):
                from .models import MenuItem
                        return MenuItem.objects.count()