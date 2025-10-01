def calculate_order_total(order_items):
        """
            Calculate the total price of an order.

                Args:
                        order_items (list of dict): Each dict should have:
                                    - 'quantity' (int or float): number of units ordered
                                                - 'price' (int or float): price per unit

                                                    Returns:
                                                            float: total cost, sum of quantity * price for all items

                                                                Handles empty order list gracefully by returning 0.0.
                                                                    """
                                                                        if not order_items:
                                                                                return 0.0

                                                                                    total = 0.0
                                                                                        for item in order_items:
                                                                                                quantity = item.get('quantity', 0)
                                                                                                        price = item.get('price', 0)
                                                                                                                total += quantity * price

                                                                                                                    return total                                                                                                                    