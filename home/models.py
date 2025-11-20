# home/models.py
from django.db import models
from django.conf import settings

class Feedback(models.Model):
    # ... existing fields ...
        user = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                        on_delete=models.SET_NULL,
                                null=True,
                                        blank=True
                                            )
                                                # ... any other fields and methods ...