# home/models.py
from django.db import models

class StaffShift(models.Model):
    staff_member = models.ForeignKey('RestaurantStaff', on_delete=models.CASCADE)
        start_time = models.DateTimeField()
            end_time = models.DateTimeField()
                date = models.DateField()

                    def __str__(self):
                            return f"{self.staff_member} - {self.date} ({self.start_time} to {self.end_time})"

                                class Meta:
                                        ordering = ['date', 'start_time']