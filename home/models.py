import datetime
from django.db import models

class ReservationManager(models.Manager):
    def get_upcoming_reservations(self):
            now = datetime.datetime.now()
                    return self.filter(reservation_datetime__gte=now)

                    class Reservation(models.Model):
                        # your existing fields here
                            reservation_datetime = models.DateTimeField()
                                # assign the custom manager
                                    objects = ReservationManager()

                                        # other methods, fields, etc.