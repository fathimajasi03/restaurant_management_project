# home/models.py
from django.db import models

class FeedbackCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
        
            def __str__(self):
                    return self.name

                    class Feedback(models.Model):
                        # ... existing fields ...
                            category = models.ForeignKey(
                                    FeedbackCategory, 
                                            on_delete=models.SET_NULL, 
                                                    null=True, 
                                                            blank=True
                                                                )