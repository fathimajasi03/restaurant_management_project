class Order(models.Model):
        # Assuming you have a status field and you want to define statuses as string constants
            STATUS_COMPLETED = 'COMPLETED'
                STATUS_PENDING = 'PENDING'  # example existing status
                    STATUS_CHOICES = [
                            (STATUS_PENDING, 'Pending'),
                                    (STATUS_COMPLETED, 'Completed'),
                                            # ... other statuses ...
                                                ]

                                                    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
                                                        # ... other fields ...

                                                            def mark_as_completed(self):
                                                                    """
                                                                            Mark this order as completed by updating the status and saving.
                                                                                    """
                                                                                            self.status = self.STATUS_COMPLETED
                                                                                                    self.save()