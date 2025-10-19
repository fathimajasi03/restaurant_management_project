from django.db import models

class Order(models.Model):
    # Existing fields (example)
        customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
            total_price = models.DecimalField(max_digits=8, decimal_places=2)
                created_at = models.DateTimeField(auto_now_add=True)
                    status = models.CharField(max_length=50)

                        # New field for customer notes
                            customer_notes = models.TextField(blank=True, null=True, help_text="Special instructions or notes from the customer")

                                def __str__(self):
                                        return f"Order #{self.id} - {self.customer.username}"