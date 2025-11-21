# home/models.py
from django.db import models

class MenuItemManager(models.Manager):
    def get_budget_items(self, max_price):
            return self.filter(price__lt=max_price)

            class MenuItem(models.Model):
                name = models.CharField(max_length=255)
                    price = models.DecimalField(max_digits=8, decimal_places=2)
                        # other fields ...

                            objects = MenuItemManager()