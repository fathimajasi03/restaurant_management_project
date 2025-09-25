from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=6, decimal_places=2)
            is_daily_special = models.BooleanField(default=False)
                # other existing fields
                