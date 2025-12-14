# home/models.py
from django.db import models

class HolidayClosure(models.Model):
    date = models.DateField()
        reason = models.CharField(max_length=255)
            is_full_day_closure = models.BooleanField(default=True)

                def __str__(self):
                        status = "Full Day Closure" if self.is_full_day_closure else "Partial Closure"
                                return f"{self.date} - {self.reason} ({status})"