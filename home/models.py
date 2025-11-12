from django.db import models

class Table(models.Model):
    # ... existing fields ...
        max_seats = models.IntegerField(default=4)  # mandatory, default to 4 seats

            # ... any other methods or fields ...