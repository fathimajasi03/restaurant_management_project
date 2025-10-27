# home/utils.py

def format_currency(amount):
    """
        Format a numeric amount as currency with a dollar sign and two decimal places.
            
                Args:
                        amount (float or Decimal): The monetary amount to format.
                            
                                Returns:
                                        str: Formatted currency string, e.g. "$12.50"
                                            """
                                                return f"${amount:,.2f}"