class Order(models.Model):
        # ...existing fields...
        
            def get_unique_item_names(self):
                    """
                            Gather all unique menu item names for this order.
                                    Returns:
                                                List of unique menu item names (list of str).
                                                        """
                                                                item_names = {
                                                                            order_item.menu_item.name
                                                                                        for order_item in self.orderitem_set.all()
                                                                                                }
                                                                                                        return list(item_names)                                                                                                                                                                          order = models.Fore         