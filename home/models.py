# home/models.py
from django.db import models

class HolidayHours(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
        date = models.DateField()
            opening_time = models.TimeField()
                closing_time = models.TimeField()
                    description = models.CharField(max_length=255, blank=True)

                        def __str__(self):
                                return f"{self.restaurant} - {self.date} ({self.description})"