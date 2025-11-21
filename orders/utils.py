# orders/utils.py

def calculate_estimated_prep_time(order_items):
    """
        Given a list of order_items (each with 'quantity' and 'prep_time_minutes'),
            returns the total preparation time in minutes as an integer.
                """
                    total_prep_time = 0
                        for item in order_items:
                                item_prep_time = item.get('prep_time_minutes', 0) * item.get('quantity', 0)
                                        total_prep_time += item_prep_time
                                            return int(total_prep_time)