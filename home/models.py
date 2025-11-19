# home/models.py
from django.db import models

class DailyOperatingHours(models.Model):
    MONDAY = 'Monday'
        TUESDAY = 'Tuesday'
            WEDNESDAY = 'Wednesday'
                THURSDAY = 'Thursday'
                    FRIDAY = 'Friday'
                        SATURDAY = 'Saturday'
                            SUNDAY = 'Sunday'

                                DAY_CHOICES = [
                                        (MONDAY, 'Monday'),
                                                (TUESDAY, 'Tuesday'),
                                                        (WEDNESDAY, 'Wednesday'),
                                                                (THURSDAY, 'Thursday'),
                                                                        (FRIDAY, 'Friday'),
                                                                                (SATURDAY, 'Saturday'),
                                                                                        (SUNDAY, 'Sunday'),
                                                                                            ]

                                                                                                restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
                                                                                                    day_of_week = models.CharField(max_length=9, choices=DAY_CHOICES)
                                                                                                        opening_time = models.TimeField()
                                                                                                            closing_time = models.TimeField()

                                                                                                                def __str__(self):
                                                                                                                        return f"{self.restaurant} - {self.day_of_week}: {self.opening_time} to {self.closing_time}"