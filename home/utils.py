# home/utils.py
from django.utils import timezone
from .models import DailyOperatingHours

def is_restaurant_open(restaurant_id):
    """
        Check if restaurant is currently open based on today's operating hours.
            
                Args:
                        restaurant_id: ID of the restaurant
                                
                                    Returns:
                                            bool: True if open, False if closed
                                                """
                                                    now = timezone.now()
                                                        today = now.date().strftime('%A')  # Gets 'Monday', 'Tuesday', etc.
                                                            current_time = now.time()
                                                                
                                                                    try:
                                                                            hours = DailyOperatingHours.objects.get(
                                                                                        restaurant_id=restaurant_id,
                                                                                                    day_of_week=today
                                                                                                            )
                                                                                                                    
                                                                                                                            return hours.opening_time <= current_time <= hours.closing_time
                                                                                                                                    
                                                                                                                                        except DailyOperatingHours.DoesNotExist:
                                                                                                                                                return False  # No hours defined for today = closed