from django.db import models

class OpeningHours(models.Model):
    DAY_CHOICES = [
            ('Monday', 'Monday'),
                    ('Tuesday', 'Tuesday'),
                            ('Wednesday', 'Wednesday'),
                                    ('Thursday', 'Thursday'),
                                            ('Friday', 'Friday'),
                                                    ('Saturday', 'Saturday'),
                                                            ('Sunday', 'Sunday'),
                                                                ]
                                                                    day = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)
                                                                        open_time = models.TimeField()
                                                                            close_time = models.TimeField()

                                                                                def __str__(self):
                                                                                        return f"{self.day}: {self.open_time} - {self.close_time}"