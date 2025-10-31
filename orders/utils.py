# orders/utils.py

def calculate_tip_amount(order_total, tip_percentage):
    """
        Calculate the tip amount based on the order total and tip percentage.
            
                Args:
                        order_total (float or Decimal): The total bill amount before the tip.
                                tip_percentage (int): The tip percentage to apply (e.g., 15 for 15%).
                                    
                                        Returns:
                                                float: The tip amount rounded to two decimal places.
                                                    """
                                                        tip_amount = order_total * (tip_percentage / 100)
                                                            return round(tip_amount, 2)