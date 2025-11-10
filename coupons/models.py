from django.db import models

class Coupon(models.Model):
    # ... existing fields ...
        is_active = models.BooleanField(default=True)