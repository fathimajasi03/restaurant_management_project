# home/models.py
from django.db import models

class MenuItemManager(models.Manager):
    def get_available_items(self):
            return self.filter(is_available=True)
            
            class MenuItem(models.Model):
                name = models.CharField(max_length=255)
                    price = models.DecimalField(max_digits=8, decimal_places=2)
                        is_available = models.BooleanField(default=True)
                            # other fields...
                            
                                objects = MenuItemManager()
                                
                                    # Alternative class method approach:
                                        # @classmethod
                                            # def get_available_items(cls):
                                                #     return cls.objects.filter(is_available=True)                       on_delete=mode                                      blank=