# orders/models.py
from django.db import models

class Order(models.Model):
    # ... your existing fields ...

        created_at = models.DateTimeField(auto_now_add=True)