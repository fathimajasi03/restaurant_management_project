from django.db import models

class Order(models.Model):
    STATUS_PENDING = 'Pending'
        STATUS_PROCESSING = 'Processing'
            STATUS_DELIVERED = 'Delivered'
                STATUS_CANCELLED = 'Cancelled'

                    STATUS_CHOICES = [
                            (STATUS_PENDING, 'Pending'),
                                    (STATUS_PROCESSING, 'Processing'),
                                            (STATUS_DELIVERED, 'Delivered'),
                                                    (STATUS_CANCELLED, 'Cancelled'),
                                                        ]

                                                            status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
                                                                # other fields ...