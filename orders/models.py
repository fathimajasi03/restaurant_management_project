from django.db import models

class Order(models.Model):
    # Your existing Order fields
        pass

        class MenuItem(models.Model):
            # Your existing MenuItem fields
                name = models.CharField(max_length=100)
                    # etc.

                    class OrderItem(models.Model):
                        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
                            menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                                quantity = models.IntegerField(default=1)
                                    price_at_time_of_order = models.DecimalField(max_digits=8, decimal_places=2)

                                        def __str__(self):
                                                return f"{self.quantity} x {self.menu_item.name}"