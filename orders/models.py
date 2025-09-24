from django.db import models
from home.models import MenuItem  # Ensure this exists

class Order(models.Model):
    # existing fields...

        def calculate_total(self):
                total = sum(
                            item.price * item.quantity
                                        for item in self.items.all()
                                                )
                                                        return total

                                                        class OrderItem(models.Model):
                                                            order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
                                                                menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                                                    quantity = models.PositiveIntegerField(default=1)
                                                                        price = models.DecimalField(max_digits=8, decimal_places=2)
                                                                        