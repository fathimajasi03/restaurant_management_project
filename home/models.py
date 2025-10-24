from django.db import models
from django.db.models import Count

class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):
            return (
                        self.get_queryset()
                                    .annotate(order_count=Count('order_items'))  # 'order_items' should be the related_name from OrderItem to MenuItem
                                                .order_by('-order_count')[:num_items]
                                                        )

                                                        class MenuItem(models.Model):
                                                            name = models.CharField(max_length=100)
                                                                # other fields...

                                                                    objects = models.Manager()        # Default manager
                                                                        top_selling = MenuItemManager()   # Custom manager for top-selling items

                                                                        class OrderItem(models.Model):
                                                                            menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_items')
                                                                                order = models.ForeignKey('Order', on_delete=models.CASCADE)
                                                                                    quantity = models.IntegerField(default=1)
                                                                                        price_at_time_of_order = models.DecimalField(max_digits=8, decimal_places=2)

                                                                                            def __str__(self):
                                                                                                    return f"{self.quantity} x {self.menu_item.name}"