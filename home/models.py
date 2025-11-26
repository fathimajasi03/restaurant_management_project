# home/models.py
from django.db import models

class MenuItem(models.Model):
    # ... your existing fields ...
        is_active = models.BooleanField(default=True)