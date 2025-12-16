# home/models.py
from django.db import models

DIETARY_CHOICES = [
    ('VEGAN', 'Vegan'),
        ('VEGETARIAN', 'Vegetarian'),
            ('GLUTEN_FREE', 'Gluten-Free'),
                ('HALAL', 'Halal'),
                    ('NONE', 'None'),
                    ]

                    class MenuItem(models.Model):
                        # ... existing fields ...
                            dietary_preference = models.CharField(
                                    max_length=20,
                                            choices=DIETARY_CHOICES,
                                                    default='NONE',
                                                            blank=True,
                                                                    null=True
                                                                        )