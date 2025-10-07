from django.db import models

class Restaurant(models.Model):
    # existing fields ...
        opening_hours = models.CharField(max_length=50, default="11:00 AM - 11:00 PM (EST)")