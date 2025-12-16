# home/models.py
from django.db import models

class Allergen(models.Model):
    name = models.CharField(max_length=100, unique=True)

        def __str__(self):
                return self.name


                class MenuItem(models.Model):
                    # ... existing fields ...
                        name = models.CharField(max_length=255)
                            price = models.DecimalField(max_digits=8, decimal_places=2)
                                # any other existing fields...

                                    allergens = models.ManyToManyField(Allergen, blank=True)

                                        def __str__(self):
                                                return self.name