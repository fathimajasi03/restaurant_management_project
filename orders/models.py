from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
            ('Pending', 'Pending'),
                    ('Processing', 'Processing'),
                            ('Cancelled', 'Cancelled'),
                                    ('Completed', 'Completed'),
                                        ]

                                            user = models.ForeignKey(User, on_delete=models.CASCADE)
                                                status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
                                                    # Other fields ...
                                                    