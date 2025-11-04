import datetime
from django.db import models

class UpcomingSpecialsManager(models.Manager):
    def upcoming(self):
            today = datetime.date.today()
                    return self.filter(date__gte=today)

                    class DailySpecial(models.Model):
                        # ... your other fields ...
                            date = models.DateField()
                                # Attach the custom manager
                                    objects = UpcomingSpecialsManager()
                                        # Optionally, keep the default manager as well:
                                            # all_objects = models.Manager()