# Model update (if needed) - orders/models.py
class Reservation(models.Model):
    STATUS_CHOICES = [
            ('pending', 'Pending'),
                    ('confirmed', 'Confirmed'),
                            ('cancelled', 'Cancelled'),
                                    ('completed', 'Completed'),
                                            ('no_show', 'No Show'),
                                                ]
                                                    # ... other fields ...
                                                        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')