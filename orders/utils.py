# orders/utils.py
from decimal import Decimal, ROUND_HALF_UP

def calculate_sales_tax(amount: Decimal, tax_rate: Decimal) -> Decimal:
    tax = (amount * tax_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return tax