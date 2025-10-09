from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=8, decimal_places=2)
            available = models.BooleanField(default=True)  # Availability field

                def __str__(self):
                        return self.name