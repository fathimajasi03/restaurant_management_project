# home/models.py
from django.db import models

class Restaurant(models.Model):
    # ... your existing fields ...
        max_capacity = models.IntegerField(null=True, blank=True)