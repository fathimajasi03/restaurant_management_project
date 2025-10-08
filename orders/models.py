class Order(models.Model):
        # ... existing fields ...

            def get_total_item_count(self):
                    """
                            Returns the total quantity of all items in this order.
                                    Assumes a related model OrderItem with a 'quantity' field.
                                            """
                                                    return sum(item.quantity for item in self.items.all())