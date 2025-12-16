# home/models.py
from django.db import models
from django.utils import timezone

class MenuItemManager(models.Manager):
    def get_discounted_items(self):
            """
                    Returns queryset of menu items with active, non-expired discounts.
                            """
                                    return self.filter(
                                                discount__is_active=True,
                                                            discount__end_date__gte=timezone.now()
                                                                    ).distinct()
                                                                    
                                                                    class MenuItem(models.Model):
                                                                        # ... existing fields ...
                                                                            discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
                                                                                
                                                                                    objects = MenuItemManager()                     class Met