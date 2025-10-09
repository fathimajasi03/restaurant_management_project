from django.db import models

class Order(models.Model):
    # ... your other fields ...
        status = models.CharField(max_length=20)
            total_amount = models.DecimalField(max_digits=10, decimal_places=2)
                # e.g., status choices: 'pending', 'completed', etc.

                    @classmethod
                        def calculate_total_revenue(cls):
                                """
                                        Aggregate and return total revenue from all completed orders.
                                                """
                                                        return cls.objects.filter(status='completed').aggregate(
                                                                    total_revenue=models.Sum('total_amount')
                                                                            )['total_revenue'] or 0