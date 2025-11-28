# home/models.py
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
        description = models.TextField()

            def __str__(self):
                    return self.name

                    class MenuItem(models.Model):
                        name = models.CharField(max_length=255)
                            price = models.DecimalField(max_digits=8, decimal_places=2)
                                is_available = models.BooleanField(default=True)
                                    ingredients = models.ManyToManyField(Ingredient, blank=True)

                                        def __str__(self):
                                                return self.name