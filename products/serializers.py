from decimal import Decimal
from django.db import models
from home.models import MenuItem
from .utils import calculate_discount  # assumes your discount logic is here

class Order(models.Model):
    # ... existing fields

        def calculate_total(self):
                total = Decimal("0.00")
                        for item in self.items.all():  # assumes related_name='items' on OrderItem
                                    price = item.price
                                                quantity = item.quantity
                                                            # Apply any discounts using your utility
                                                                        discounted_price = calculate_discount(item, price)
                                                                                    total += discounted_price * quantity
                                                                                            return total

                                                                                            class OrderItem(models.Model):
                                                                                                order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
                                                                                                    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                                                                                        quantity = models.PositiveIntegerField(default=1)
                                                                                                            price = models.DecimalField(max_digits=8, decimal_places=2)
                                                                                                                # add discount or other fields if needed
                                                                                                                