# home/utils.py
from django.utils import timezone
from .models import HolidayClosure
from datetime import date

def is_restaurant_closed_on_holiday(date_to_check):
    """
        Check if restaurant is closed on a specific date due to holiday.
            
                Args:
                        date_to_check: date object to check
                                
                                    Returns:
                                            bool: True if closed for full day, False otherwise
                                                """
                                                    return HolidayClosure.objects.filter(
                                                            date=date_to_check,
                                                                    is_full_day_closure=True
                                                                        ).exists()