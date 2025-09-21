from django.contrib.auth.models import User
from django.db import models

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
        product_name = models.CharField(max_length=255)
            quantity = models.PositiveIntegerField()
                price = models.DecimalField(max_digits=8, decimal_places=2)

                class Order(models.Model):
                    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
                        order_date = models.DateTimeField(auto_now_add=True)
                            total_price = models.DecimalField(max_digits=10, decimal_places=2)
                            
                                              