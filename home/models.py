from django.db import models

class Restaurant(models.Model):
    # ... existing fields ...
        has_delivery = models.BooleanField(default=False, help_text="Does the restaurant offer delivery services?")