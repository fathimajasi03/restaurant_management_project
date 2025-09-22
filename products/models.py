from django.db import models
from django.contrib.auth.models import User
from home.models import MenuItem  # assuming home app has MenuItem model

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
        order_date = models.DateTimeField(auto_now_add=True)
            total_price = models.DecimalField(max_digits=10, decimal_places=2)

            class OrderItem(models.Model):
                order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
                    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
                        quantity = models.PositiveIntegerField()
                            price = models.DecimalField(max_digits=8, decimal_places=2)
                            