# home/utils.py
from decimal import Decimal

def format_price(price, currency_symbol='$'):
    """
        Format a price value as currency string with 2 decimal places.
            
                Args:
                        price: float or Decimal value
                                currency_symbol: currency symbol (default: '$')
                                    
                                        Returns:
                                                str: formatted currency string
                                                    """
                                                        price = Decimal(str(price)).quantize(Decimal('0.00'))
                                                            return f"{currency_symbol}{price}"